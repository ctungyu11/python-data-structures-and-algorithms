"""
## summary:
This module contains classes that represent linked lists.

## classes:
- Node: A class representing a node in a linked list.
- LinkedList: A class representing a doubly linked list.
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    """A class representing a node in a linked list."""
    value: any
    next: Optional["Node"] = None
    prev: Optional["Node"] = None


class LinkedList:
    """A class representing a doubly linked list."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self._current = None  # Used for iteration
        
    def append_left(self, value: int) -> None:
        """Append a node with the given value to the left of the list."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    def append_right(self, value: int) -> None:
        """Append a node with the given value to the right of the list."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def pop_left(self) -> any:
        """Remove and return the value of the leftmost node in the list."""
        if self.head is None:
            raise ValueError("List is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        
        self.size -= 1
        return value
    
    def pop_right(self) -> any:
        """Remove and return the value of the rightmost node in the list."""
        if self.head is None:
            raise ValueError("List is empty")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        
        self.size -= 1
        return value
    
    def insert(self, index: int, value: any) -> None:
        """Insert a node with the given value at the specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.append_left(value)
        elif index == self.size:
            self.append_right(value)
        else:
            current = self._get_node(index)
            node = Node(value)
            current.prev.next = node
            node.prev = current.prev
            node.next = current
            current.prev = node
            self.size += 1
    
    def __contains__(self, value: any) -> bool:
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
    
    def __iter__(self):
        self._current = self.head
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value
    
    def __getitem__(self, index: int) -> any:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        return self._get_node(index).value
    
    def _get_node(self, index: int) -> Node:
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __setitem__(self, index: int, value: any) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        self._get_node(index).value = value
    
    def __delitem__(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        node = self._get_node(index)
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        
        self.size -= 1

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append_right(1)
    linked_list.append_right(2)
    linked_list.append_right(3)
    linked_list.append_right(4)
    linked_list.append_right(5)
    print(linked_list)  # 1 -> 2 -> 3 -> 4 -> 5
    print(len(linked_list))  # 5
    
    linked_list.append_left(0)
    print(linked_list)  # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    print(len(linked_list))  # 6
    
    linked_list.pop_left()
    linked_list.pop_right()
    print(linked_list)  # 1 -> 2 -> 3 -> 4
    print(len(linked_list))  # 4
    
    linked_list[0] = 0
    linked_list[3] = 5
    del linked_list[1]
    print(linked_list)  # 0 -> 3 -> 5
    print(linked_list[0])  # 0
    print(linked_list[1])  # 3
    print(linked_list[2])  # 5
    
    print(0 in linked_list)  # True
    print(1 in linked_list)  # False
    
    linked_list.insert(1, 2)
    print(linked_list)
    