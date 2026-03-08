"""
created on 2026-03-07 17:14:49
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
import random

heads = 0
tails = 0
def coinflip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

for i in range(10_000):
    if coinflip() == "heads":
        heads = heads + 1
    else:
        tails = tails + 1
print(f"{heads} and {tails}")
ratio = heads / tails
print(F"ratio heads to tails is {ratio}")


# heads = 0
# tails = 0
# def coinflip(x):
#     h, t = 0, 0  # Local counters
#     for i in range(x):
#         flip = random.randint(0, 1)
#         if flip == 0:
#             h += 1
#         else:
#             t += 1
#     return h, t

# heads, tails = coinflip(10_000)
# print(f"heads: {heads} tails: {tails}")
