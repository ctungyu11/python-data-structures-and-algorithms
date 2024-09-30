"""
## Bubble Sort

### Description
Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order. The time
complexity of bubble sort is O(n^2) in the worst case.
"""

from typing import List, Callable


def bubble_sort(arr: List[any], key: Callable[[any, any], bool] = lambda x, y: x < y) -> List[any]:
    """Sort the array using bubble sort."""
    new_arr = arr.copy()
    
    n = len(new_arr)
    for i in range(n):
        for j in range(n - i - 1):
            if not key(new_arr[j], new_arr[j + 1]):
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
