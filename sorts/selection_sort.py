"""
## Selection Sort

### Description
Selection sort is a simple sorting algorithm that repeatedly finds the minimum element
from the unsorted part of the array and puts it at the beginning. The time complexity
of selection sort is O(n^2) in the worst case.
"""

from typing import List, Callable


def selection_sort(arr: List[any], cmp: Callable[[any, any], bool] = lambda x, y: x < y) -> List[any]:
    """Sort the array using selection sort."""
    new_arr = arr.copy()
    n = len(new_arr)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if not cmp(new_arr[min_idx], new_arr[j]):
                min_idx = j
        
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
    
    return new_arr


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
