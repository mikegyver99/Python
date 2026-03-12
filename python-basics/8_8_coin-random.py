# -*- coding: utf-8 -*-
"""
created on 2026-03-08 18:01:41
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Write a function that simulates flipping a coin and if get same result flip again.
# Count how many matching flips happen. Once different value is the result. restart the series.
#

import random
def single_series():
    """Simulate repeatedly flipping a coin until both heads and tails are seen."""
    flip_result = random.randint(0, 1)
    flip_count = 1
    while flip_result == random.randint(0, 1):
        flip_count += 1
    # The last step in the loop flipped the coin but didn't update the tally,
    # so we need to increase the flip_count by 1
    flip_count = flip_count + 1
    return flip_count

def avg_series(num_trials):
    """Calculate the average number of flips per trial over num_trials total trials."""
    total = 0
    for trial in range(num_trials):
        total = total + single_series()
    return total / num_trials

print(f"The average is {avg_series(10_000)}")
