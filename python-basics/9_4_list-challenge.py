# -*- coding: utf-8 -*-
"""
created on 2026-03-09 14:23:08
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""

universities = [
    ['California Institue of Technology', 2175, 37704],
    ['Harvard', 19697, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(list_of_universities):
    stu_total = 0
    stu_list = []
    tut_total = 0
    tut_list = []
    for stu in list_of_universities:
        stu_num = stu[1]
        stu_list.append(stu[1])
        stu_tut = stu[2]
        stu_total = stu_total + stu_num
        tut_list.append(stu[2])
        tut_total = tut_total + stu_tut
    return stu_total, stu_list, tut_total, tut_list

def mean(values):
    return sum(values) / len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        left_index = (len(values) - 1) // 2
        right_index = (len(values) + 1) // 2
        return mean([values[left_index], values[right_index]])

stu_total, stu_list, tut_total, tut_list = enrollment_stats(universities)
stu_mean_value = mean(stu_list)
stu_median_value = median(stu_list)
tut_mean_value = mean(tut_list)
tut_median_value = median(tut_list)
print("******" * 6)
print(f"Total students: {stu_total:,}")
print(f"Total tutition: $ {tut_total:,}")
print(f"\nStudent mean: {stu_mean_value:,.2f}")
print(f"Student median: {stu_median_value:,}")
print(f"\nTuition mean: $ {tut_mean_value:,.2f}")
print(f"Tuition median: $ {tut_median_value:,}")
print("******" * 6)