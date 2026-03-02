#!/usr/bin/env python3
"""
# ============================================================================
# MIT License
#
# Copyright (c) 2025 mikegyvergarcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ============================================================================
#
# DISCLAIMER: This script modifies live AWS resources by creating or updating
# tags.  Always test in a non-production environment first.  The authors accept
# no responsibility for unintended changes, costs, or outages resulting from
# use of this script.  You are responsible for ensuring your AWS IAM permissions
# follow the principle of least privilege before running this tool.
# ============================================================================

aws_tag_enforcer.py
-------------------
Scans AWS resources for a missing or empty "prj_code" tag and creates/updates
it with a supplied value.

Usage:
    python aws_tag_enforcer.py <resource_type> <prj_code_value>

Supported resource types (case-insensitive):
    ec2, s3, rds, lambda, dynamodb, sqs, sns, ecs, eks, elb, elbv2,
    cloudformation, secretsmanager, kms

Examples:
    python aws_tag_enforcer.py ec2 my-project-cost-center
    python aws_tag_enforcer.py s3  my-project-cost-center
    python aws_tag_enforcer.py rds my-project-cost-center

Authentication:
    Uses the standard boto3 credential chain (env vars, ~/.aws/credentials,
    IAM instance profile, etc.).  Set AWS_PROFILE / AWS_DEFAULT_REGION as
    needed before running.

Requirements:
    pip install boto3
    Python 3.13+
"""

import argparse
import logging
import sys
from typing import Callable

import boto3
from botocore.exceptions import ClientError

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

# The tag key we are enforcing across all resource types.
TAG_KEY = "prj_code"


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def needs_tagging(tags: list[dict] | None) -> bool:
    """
    Return True when the 'prj_code' tag is absent OR its value is blank/empty.
    Tags are expected in the standard AWS list-of-dicts format:
        [{"Key": "...", "Value": "..."}, ...]
    """
    if not tags:
        return True
    for tag in tags:
        if tag.get("Key") == TAG_KEY:
            return not tag.get("Value", "").strip()
    return True  # key not found at all


def paginate(client, method: str, result_key: str, **kwargs):
    """
    Generic paginator wrapper for APIs that use NextToken / Marker / etc.
    Yields individual items from the list identified by result_key.
    """
    paginator = client.get_paginator(method)
    for page in paginator.paginate(**kwargs):
        yield from page.get(result_key, [])


# ---------------------------------------------------------------------------
# Per-service tagging handlers
# Each handler receives (session, prj_code_value) and returns
# (checked: int, tagged: int).
# ---------------------------------------------------------------------------

def handle_ec2(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Iterate over all EC2 instances (any state) and tag those missing prj_code.
    EC2 also covers VPCs, subnets, security groups, volumes, etc. but here we
    focus on instances as the most common resource.  Extend the resource_types
    list below to broaden coverage.
    """
    ec2 = session.client("ec2")
    checked = tagged = 0

    # Describe all instances across all reservations.
    response = ec2.describe_instances()
    reservations = response.get("Reservations", [])

    # Handle pagination manually (EC2 describe_instances uses NextToken).
    while True:
        for reservation in reservations:
            for instance in reservation.get("Instances", []):
                checked += 1
                instance_id = instance["InstanceId"]
                if needs_tagging(instance.get("Tags")):
                    log.info("Tagging EC2 instance %s", instance_id)
                    ec2.create_tags(
                        Resources=[instance_id],
                        Tags=[{"Key": TAG_KEY, "Value": value}],
                    )
                    tagged += 1

        # Follow pagination token if present.
        next_token = response.get("NextToken")
        if not next_token:
            break
        response = ec2.describe_instances(NextToken=next_token)
        reservations = response.get("Reservations", [])

    return checked, tagged


def handle_s3(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List all S3 buckets and apply the tag to any bucket missing prj_code.
    S3 uses a separate get_bucket_tagging call per bucket because the ListBuckets
    API does not return tags inline.
    """
    s3 = session.client("s3")
    checked = tagged = 0

    buckets = s3.list_buckets().get("Buckets", [])
    for bucket in buckets:
        name = bucket["Name"]
        checked += 1
        try:
            existing = s3.get_bucket_tagging(Bucket=name).get("TagSet", [])
        except ClientError as exc:
            # NoSuchTagSet is expected when a bucket has no tags at all.
            if exc.response["Error"]["Code"] == "NoSuchTagSet":
                existing = []
            else:
                log.warning("Could not read tags for bucket %s: %s", name, exc)
                continue

        if needs_tagging(existing):
            log.info("Tagging S3 bucket %s", name)
            # S3 tagging replaces the entire tag set, so we must preserve existing tags.
            updated_tags = [t for t in existing if t["Key"] != TAG_KEY]
            updated_tags.append({"Key": TAG_KEY, "Value": value})
            s3.put_bucket_tagging(
                Bucket=name,
                Tagging={"TagSet": updated_tags},
            )
            tagged += 1

    return checked, tagged


def handle_rds(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Iterate over all RDS DB instances and clusters, tagging those without prj_code.
    RDS uses ARNs for tagging via add_tags_to_resource.
    """
    rds = session.client("rds")
    checked = tagged = 0

    # ----- DB Instances -----
    for db in paginate(rds, "describe_db_instances", "DBInstances"):
        checked += 1
        arn = db["DBInstanceArn"]
        tags = rds.list_tags_for_resource(ResourceName=arn).get("TagList", [])
        if needs_tagging(tags):
            log.info("Tagging RDS instance %s", db["DBInstanceIdentifier"])
            rds.add_tags_to_resource(
                ResourceName=arn,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    # ----- DB Clusters (Aurora etc.) -----
    for cluster in paginate(rds, "describe_db_clusters", "DBClusters"):
        checked += 1
        arn = cluster["DBClusterArn"]
        tags = rds.list_tags_for_resource(ResourceName=arn).get("TagList", [])
        if needs_tagging(tags):
            log.info("Tagging RDS cluster %s", cluster["DBClusterIdentifier"])
            rds.add_tags_to_resource(
                ResourceName=arn,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    return checked, tagged


def handle_lambda(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Enumerate all Lambda functions and tag those missing prj_code.
    Lambda returns tags inline from list_functions, but tag format is a plain
    dict rather than a list of Key/Value pairs.
    """
    lam = session.client("lambda")
    checked = tagged = 0

    for fn in paginate(lam, "list_functions", "Functions"):
        checked += 1
        fn_name = fn["FunctionName"]
        # Lambda tags are returned as {"key": "value"} dicts, not Key/Value pairs.
        tags_dict: dict = lam.list_tags(Resource=fn["FunctionArn"]).get("Tags", {})
        existing_value = tags_dict.get(TAG_KEY, "").strip()
        if not existing_value:
            log.info("Tagging Lambda function %s", fn_name)
            lam.tag_resource(
                Resource=fn["FunctionArn"],
                Tags={TAG_KEY: value},
            )
            tagged += 1

    return checked, tagged


def handle_dynamodb(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Scan all DynamoDB tables and apply the tag where missing.
    DynamoDB requires an ARN for tag operations, obtained via describe_table.
    """
    ddb = session.client("dynamodb")
    checked = tagged = 0

    for table_name in paginate(ddb, "list_tables", "TableNames"):
        checked += 1
        arn = ddb.describe_table(TableName=table_name)["Table"]["TableArn"]
        tags = ddb.list_tags_of_resource(ResourceArn=arn).get("Tags", [])
        if needs_tagging(tags):
            log.info("Tagging DynamoDB table %s", table_name)
            ddb.tag_resource(
                ResourceArn=arn,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    return checked, tagged


def handle_sqs(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List all SQS queues and tag those without prj_code.
    SQS tags are fetched via list_queue_tags and applied via tag_queue.
    """
    sqs = session.client("sqs")
    checked = tagged = 0

    for queue_url in paginate(sqs, "list_queues", "QueueUrls"):
        checked += 1
        tags_dict: dict = sqs.list_queue_tags(QueueUrl=queue_url).get("Tags", {})
        existing_value = tags_dict.get(TAG_KEY, "").strip()
        if not existing_value:
            log.info("Tagging SQS queue %s", queue_url.split("/")[-1])
            sqs.tag_queue(
                QueueUrl=queue_url,
                Tags={TAG_KEY: value},
            )
            tagged += 1

    return checked, tagged


def handle_sns(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List all SNS topics and tag those without prj_code.
    SNS returns tags as Key/Value list pairs via list_tags_for_resource.
    """
    sns = session.client("sns")
    checked = tagged = 0

    for topic in paginate(sns, "list_topics", "Topics"):
        arn = topic["TopicArn"]
        checked += 1
        tags = sns.list_tags_for_resource(ResourceArn=arn).get("Tags", [])
        if needs_tagging(tags):
            log.info("Tagging SNS topic %s", arn.split(":")[-1])
            sns.tag_resource(
                ResourceArn=arn,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    return checked, tagged


def handle_ecs(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Enumerate ECS clusters and their services, tagging any that lack prj_code.
    ECS supports new-style ARN tagging; ensure your account has this enabled.
    """
    ecs = session.client("ecs")
    checked = tagged = 0

    # Gather all cluster ARNs first.
    cluster_arns: list[str] = []
    for arn in paginate(ecs, "list_clusters", "clusterArns"):
        cluster_arns.append(arn)

    # Tag clusters themselves.
    for arn in cluster_arns:
        checked += 1
        tags = ecs.list_tags_for_resource(resourceArn=arn).get("tags", [])
        # ECS returns tags as {"key": ..., "value": ...} (lowercase keys).
        existing_value = next(
            (t["value"] for t in tags if t.get("key") == TAG_KEY), ""
        ).strip()
        if not existing_value:
            log.info("Tagging ECS cluster %s", arn.split("/")[-1])
            ecs.tag_resource(
                resourceArn=arn,
                tags=[{"key": TAG_KEY, "value": value}],
            )
            tagged += 1

        # Tag services within the cluster.
        for svc_arn in paginate(ecs, "list_services", "serviceArns", cluster=arn):
            checked += 1
            svc_tags = ecs.list_tags_for_resource(resourceArn=svc_arn).get("tags", [])
            svc_value = next(
                (t["value"] for t in svc_tags if t.get("key") == TAG_KEY), ""
            ).strip()
            if not svc_value:
                log.info("Tagging ECS service %s", svc_arn.split("/")[-1])
                ecs.tag_resource(
                    resourceArn=svc_arn,
                    tags=[{"key": TAG_KEY, "value": value}],
                )
                tagged += 1

    return checked, tagged


def handle_eks(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List ECS clusters and tag those without prj_code.
    EKS tags are standard Key/Value pairs.
    """
    eks = session.client("eks")
    checked = tagged = 0

    for cluster_name in paginate(eks, "list_clusters", "clusters"):
        checked += 1
        cluster = eks.describe_cluster(name=cluster_name)["cluster"]
        tags_dict: dict = cluster.get("tags", {})
        existing_value = tags_dict.get(TAG_KEY, "").strip()
        if not existing_value:
            log.info("Tagging EKS cluster %s", cluster_name)
            eks.tag_resource(
                resourceArn=cluster["arn"],
                tags={TAG_KEY: value},
            )
            tagged += 1

    return checked, tagged


def handle_elb(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Classic (v1) Elastic Load Balancers — tag those missing prj_code.
    """
    elb = session.client("elb")
    checked = tagged = 0

    lb_names = [
        lb["LoadBalancerName"]
        for lb in paginate(elb, "describe_load_balancers", "LoadBalancerDescriptions")
    ]

    # describe_tags accepts up to 20 names at a time.
    chunk_size = 20
    for i in range(0, len(lb_names), chunk_size):
        chunk = lb_names[i : i + chunk_size]
        tag_descriptions = elb.describe_tags(LoadBalancerNames=chunk).get(
            "TagDescriptions", []
        )
        for td in tag_descriptions:
            checked += 1
            if needs_tagging(td.get("Tags")):
                log.info("Tagging classic ELB %s", td["LoadBalancerName"])
                elb.add_tags(
                    LoadBalancerNames=[td["LoadBalancerName"]],
                    Tags=[{"Key": TAG_KEY, "Value": value}],
                )
                tagged += 1

    return checked, tagged


def handle_elbv2(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Application / Network / Gateway Load Balancers (ELBv2).
    Also tags associated Target Groups.
    """
    elbv2 = session.client("elbv2")
    checked = tagged = 0

    # ----- Load Balancers -----
    lb_arns = [
        lb["LoadBalancerArn"]
        for lb in paginate(elbv2, "describe_load_balancers", "LoadBalancers")
    ]
    chunk_size = 20
    for i in range(0, len(lb_arns), chunk_size):
        chunk = lb_arns[i : i + chunk_size]
        for td in elbv2.describe_tags(ResourceArns=chunk).get("TagDescriptions", []):
            checked += 1
            if needs_tagging(td.get("Tags")):
                log.info("Tagging ELBv2 %s", td["ResourceArn"].split("/")[-2])
                elbv2.add_tags(
                    ResourceArns=[td["ResourceArn"]],
                    Tags=[{"Key": TAG_KEY, "Value": value}],
                )
                tagged += 1

    # ----- Target Groups -----
    tg_arns = [
        tg["TargetGroupArn"]
        for tg in paginate(elbv2, "describe_target_groups", "TargetGroups")
    ]
    for i in range(0, len(tg_arns), chunk_size):
        chunk = tg_arns[i : i + chunk_size]
        for td in elbv2.describe_tags(ResourceArns=chunk).get("TagDescriptions", []):
            checked += 1
            if needs_tagging(td.get("Tags")):
                log.info("Tagging target group %s", td["ResourceArn"].split(":")[-1])
                elbv2.add_tags(
                    ResourceArns=[td["ResourceArn"]],
                    Tags=[{"Key": TAG_KEY, "Value": value}],
                )
                tagged += 1

    return checked, tagged


def handle_cloudformation(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    Iterate over all CloudFormation stacks (excluding nested stacks) and tag
    those that are missing prj_code.  Nested stacks inherit tags from their
    parent, so we skip them to avoid double-tagging.
    """
    cf = session.client("cloudformation")
    checked = tagged = 0

    for stack in paginate(cf, "describe_stacks", "Stacks"):
        # Skip nested stacks — they are managed by their root stack.
        if stack.get("ParentId"):
            continue
        checked += 1
        stack_name = stack["StackName"]
        if needs_tagging(stack.get("Tags")):
            log.info("Tagging CloudFormation stack %s", stack_name)
            # CloudFormation requires re-submitting the full parameter set to
            # update tags.  We use UPDATE_TERMINATION_PROTECTION as the minimal
            # no-op if the stack is stable; tagging via update_stack is safer.
            # NOTE: update_stack may trigger a stack update cycle.  For
            # read-only tagging consider using the Resource Groups Tagging API.
            try:
                cf.update_termination_protection(
                    EnableTerminationProtection=stack.get(
                        "EnableTerminationProtection", False
                    ),
                    StackName=stack_name,
                )
                # Use the Resource Groups Tagging API for a non-disruptive tag.
                rgt = session.client("resourcegroupstaggingapi")
                rgt.tag_resources(
                    ResourceARNList=[stack["StackId"]],
                    Tags={TAG_KEY: value},
                )
                tagged += 1
            except ClientError as exc:
                log.warning("Could not tag stack %s: %s", stack_name, exc)

    return checked, tagged


def handle_secretsmanager(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List Secrets Manager secrets and tag those missing prj_code.
    Secrets Manager tags are Key/Value pairs.
    """
    sm = session.client("secretsmanager")
    checked = tagged = 0

    for secret in paginate(sm, "list_secrets", "SecretList"):
        checked += 1
        arn = secret["ARN"]
        tags = secret.get("Tags", [])
        if needs_tagging(tags):
            log.info("Tagging secret %s", secret["Name"])
            sm.tag_resource(
                SecretId=arn,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    return checked, tagged


def handle_kms(session: boto3.Session, value: str) -> tuple[int, int]:
    """
    List customer-managed KMS keys and tag those missing prj_code.
    AWS-managed keys (alias/aws/*) are skipped as they cannot be tagged.
    """
    kms = session.client("kms")
    checked = tagged = 0

    for key_meta in paginate(kms, "list_keys", "Keys"):
        key_id = key_meta["KeyId"]
        # Retrieve full metadata to filter out AWS-managed keys.
        desc = kms.describe_key(KeyId=key_id)["KeyMetadata"]
        if desc.get("KeyManager") != "CUSTOMER":
            continue  # skip AWS-managed or AWS-owned keys
        checked += 1
        tags = kms.list_resource_tags(KeyId=key_id).get("Tags", [])
        if needs_tagging(tags):
            log.info("Tagging KMS key %s", key_id)
            kms.tag_resource(
                KeyId=key_id,
                Tags=[{"Key": TAG_KEY, "Value": value}],
            )
            tagged += 1

    return checked, tagged


# ---------------------------------------------------------------------------
# Dispatch table: maps CLI resource type strings to handler functions.
# Add new services here without touching argument parsing or main logic.
# ---------------------------------------------------------------------------
HANDLERS: dict[str, Callable[[boto3.Session, str], tuple[int, int]]] = {
    "ec2":              handle_ec2,
    "s3":               handle_s3,
    "rds":              handle_rds,
    "lambda":           handle_lambda,
    "dynamodb":         handle_dynamodb,
    "sqs":              handle_sqs,
    "sns":              handle_sns,
    "ecs":              handle_ecs,
    "eks":              handle_eks,
    "elb":              handle_elb,
    "elbv2":            handle_elbv2,
    "cloudformation":   handle_cloudformation,
    "secretsmanager":   handle_secretsmanager,
    "kms":              handle_kms,
}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Enforce the 'prj_code' tag on AWS resources.\n"
            "Scans the specified resource type and creates/updates the tag\n"
            "where it is absent or blank."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Supported resource types:\n  "
            + "\n  ".join(sorted(HANDLERS.keys()))
        ),
    )
    parser.add_argument(
        "resource_type",
        metavar="RESOURCE_TYPE",
        choices=HANDLERS.keys(),
        help="AWS resource type to scan (e.g. ec2, s3, rds).",
    )
    parser.add_argument(
        "prj_code_value",
        metavar="PRJ_CODE_VALUE",
        help="Value to set for the 'prj_code' tag on untagged resources.",
    )
    parser.add_argument(
        "--profile",
        default=None,
        help="AWS CLI profile name to use (optional).",
    )
    parser.add_argument(
        "--region",
        default=None,
        help="AWS region to target (optional; falls back to env/config).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Create a boto3 session, optionally scoped to a profile and/or region.
    session = boto3.Session(
        profile_name=args.profile,
        region_name=args.region,
    )

    log.info(
        "Starting tag enforcement: resource_type=%s  tag=%s=%s  region=%s",
        args.resource_type,
        TAG_KEY,
        args.prj_code_value,
        session.region_name or "default",
    )

    # Look up and call the appropriate handler from the dispatch table.
    handler = HANDLERS[args.resource_type]
    try:
        checked, tagged = handler(session, args.prj_code_value)
    except ClientError as exc:
        log.error("AWS API error: %s", exc)
        sys.exit(1)

    log.info(
        "Done. Resources checked: %d  |  Resources tagged/updated: %d",
        checked,
        tagged,
    )


if __name__ == "__main__":
    main()