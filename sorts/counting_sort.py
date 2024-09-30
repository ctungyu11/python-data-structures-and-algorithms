"""
## Counting Sort

### Description
Counting sort is a sorting algorithm that sorts the elements of an array by counting the
number of occurrences of each unique element in the array and then sorting them based on
their frequencies. The time complexity of counting sort is O(n + k), where n is the number
of elements in the array and k is the range of the input.
"""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """Sort the array using counting sort."""
    n = len(arr)
    if n <= 1:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    
    counts = [0] * (max_val - min_val + 1)
    for num in arr:
        counts[num - min_val] += 1
    
    sorted_arr = []
    for i, freq in enumerate(counts):
        if freq == 0:
            continue
        sorted_arr += [i + min_val] * freq

    return sorted_arr        


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(counting_sort(nums))  # [11, 12, 22, 25, 34, 64, 90]
