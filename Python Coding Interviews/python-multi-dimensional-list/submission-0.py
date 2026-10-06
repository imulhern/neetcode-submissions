from typing import List
from math import inf

def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maxes = []
    for l in nested_arr: 
        l_max = -inf
        for e in l:
            l_max = max(l_max,e)
        maxes.append(l_max)
    return maxes


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
