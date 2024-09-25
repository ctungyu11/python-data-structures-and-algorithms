"""_summary_:
This module contains classes that represent linked lists.

_classes_:
- Node: A class representing a node in a linked list.
- LinkedList: A class representing a doubly linked list.

_functions_:
- from_list: Create a linked list from a list of values.
- to_list: Create a list of values from a linked list.
- reverse: Reverse a linked list.
- copy: Create a copy of a linked list.
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


def from_list(values: list) -> LinkedList:
    """Create a linked list from a list of values."""
    linked_list = LinkedList()
    for value in values:
        linked_list.append_right(value)
    return linked_list


def to_list(linked_list: LinkedList) -> list:
    """Create a list of values from a linked list."""
    return [value for value in linked_list]


def reverse(linked_list: LinkedList) -> LinkedList:
    """Reverse a linked list."""
    reversed_list = LinkedList()
    current = linked_list.tail
    while current is not None:
        reversed_list.append_right(current.value)
        current = current.prev
    return reversed_list


def copy(linked_list: LinkedList) -> LinkedList:
    """Create a copy of a linked list."""
    linked_list_copy = LinkedList()
    current = linked_list.head
    while current is not None:
        linked_list_copy.append_right(current.value)
        current = current.next


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
    
    reversed_list = reverse(linked_list)
    print(reversed_list)  # 4 -> 3 -> 2 -> 1
    print(to_list(reversed_list))  # [4, 3, 2, 1]
    
    linked_list = from_list([1, 2, 3, 4, 5])
    print(linked_list)  # 1 -> 2 -> 3 -> 4 -> 5
    print(to_list(linked_list))  # [1, 2, 3, 4, 5]
    
    for value in linked_list:
        print(value)

    linked_list2 = copy(linked_list)
    linked_list2.append_right(6)
    print(linked_list) # 1 -> 2 -> 3 -> 4 -> 5
    