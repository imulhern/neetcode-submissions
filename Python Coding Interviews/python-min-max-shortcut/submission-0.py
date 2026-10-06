from typing import List
from math import inf

def disallow_negatives(num: int) -> int:
    if 0 <= num: 
        return num 
    return 0


def max_difference(nums: List[int]) -> int:
    max_diff = -inf
    for i,x in enumerate(nums):
        if i >= 1:
            diff = nums[i] - nums[i-1]
            max_diff = max(diff,max_diff)
    return max_diff




# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
