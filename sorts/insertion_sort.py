"""
## Insertion Sort

### Description
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
and it is efficient for small data sets. The time complexity of insertion sort is O(n^2) in the worst case.
"""

from typing import List, Callable


def insertion_sort(arr: List[any], cmp: Callable[[any, any], bool] = lambda x, y: x < y) -> List[any]:
    """Sort the array using insertion sort."""
    new_arr = arr.copy()
    
    n = len(new_arr)
    for i in range(1, n):
        key = new_arr[i]
        j = i - 1
        while j >= 0 and not cmp(new_arr[j], key):
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = key
    return new_arr


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
