"""
## summary:
This module contains classes that represent binary heaps.

## classes:
- Heap: A class representing a binary heap.

## description:
A binary heap is a complete binary tree where each node has a value more extreme than or equal to its children.
The Heap class is a binary heap that can be used as a priority queue.
It has the following methods:
- insert(value: any) -> None: Insert a value into the heap.
- top() -> any: Return the top value in the heap.
- pop() -> any: Remove and return the top value in the heap.

## example:
```python
from heap import Heap

priority_queue = Heap()
priority_queue.insert(3)
priority_queue.insert(1)
priority_queue.insert(2)
print(priority_queue.pop())  # 1
print(priority_queue.pop())  # 2
print(priority_queue.pop())  # 3
```
"""


from typing import List, Callable


class Heap:
    """A class representing a binary heap."""
    
    def __init__(self, cmp: Callable[[any, any], bool] = lambda x, y: x < y):
        self._heap: List[any] = []
        self._cmp = cmp
    
    def insert(self, value: any) -> None:
        """Insert a value into the heap."""
        self._heap.append(value)
        self._heapify_up(len(self._heap) - 1)
    
    def top(self) -> any:
        """Return the top value in the heap."""
        if len(self._heap) == 0:
            raise ValueError("Heap is empty")
        return self._heap[0]
    
    def pop(self) -> any:
        """Remove and return the top"""
        if len(self._heap) == 0:
            raise ValueError("Heap is empty")
        
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        self._heapify_down(0)
        return value
    
    def _heapify_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if not self._cmp(self._heap[index], self._heap[parent]):
                return
                
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
        
    def _heapify_down(self, index: int) -> None:
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            extrema = index
            if left < len(self._heap) and self._cmp(self._heap[left], self._heap[extrema]):
                extrema = left
            if right < len(self._heap) and self._cmp(self._heap[right], self._heap[extrema]):
                extrema = right
            
            if extrema == index:
                return
            self._heap[index], self._heap[extrema] = self._heap[extrema], self._heap[index]
            index = extrema
        
    def __len__(self):
        return len(self._heap)


if __name__ == "__main__":
    pq = Heap()
    pq.insert(3)
    pq.insert(1)
    pq.insert(2)
    
    while len(pq) > 0:
        print(pq.pop())
    
    pq2 = Heap(lambda x, y: x > y)
    pq2.insert(3)
    pq2.insert(1)
    pq2.insert(1)
    pq2.insert(2)
    
    print(pq2.pop())
    print(pq2.pop())
    print(pq2.pop())
    print(pq2.pop())
