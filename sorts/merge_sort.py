"""
## Merge Sort

### Description
Merge sort is a divide-and-conquer algorithm that divides the input array into two halves,
recursively sorts the two halves, and then merges the sorted halves. The time complexity
of merge sort is O(n log n) in the worst case.
"""

from typing import List, Callable


def merge_sort(arr: List[any], key: Callable[[any, any], bool] = lambda x, y: x < y) -> List[any]:
    """Sort the array using merge sort."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    
    i, j = 0, 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        if key(left[i], right[j]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    
    return sorted_arr


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
