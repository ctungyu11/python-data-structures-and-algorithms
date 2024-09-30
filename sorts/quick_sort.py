"""
## Quick Sort

### Description
Quick sort is a divide-and-conquer algorithm that selects a pivot element and partitions the input
array around the pivot such that all elements less than the pivot are on the left and all elements
greater than the pivot are on the right. It then recursively sorts the two partitions. The time
complexity of quick sort is O(n log n) in the average case and O(n^2) in the worst case.
"""

from typing import List, Callable


def quick_sort(arr: List[any], key: Callable[[any, any], bool] = lambda x, y: x < y) -> List[any]:
    """Sort the array using quick sort."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x, pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if key(pivot, x)]
    
    return quick_sort(left, key) + middle + quick_sort(right, key)


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(quick_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
    