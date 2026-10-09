import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = []
    [heapq.heappush(heap, num) for num in arr]
    return heapq.nsmallest(1, heap)[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    heap = []
    [heapq.heappush(heap, num) for num in arr]
    return heapq.nsmallest(4, heap)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    # heap = []
    # max_heap = []

    # [heapq.heappush(heap, num) for num in arr]
    # for n in heapq.nsmallest(2, heap):
    #     heapq.heappush(max_heap, -num)
    # min_2 = []
    # while max_heap:
    #     min_2.append(-heapq.heappop(max_heap))
    # return min_2
    min_2 = heapq.nsmallest(2, arr)
    return min_2[::-1] # reverse the list


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))
