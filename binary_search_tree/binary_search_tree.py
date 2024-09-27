"""
## summary:
The module contains classes that represent binary search trees.

## classes:
- Node: A class representing a node in a binary search tree.
- BinarySearchTree: A class representing a binary search tree (no repeated elements).
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    """A class representing a node in a binary search tree."""
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    """A class representing a binary search tree."""
    
    def __init__(self):
        self.root = None
        self.size = 0

        self._current = None  # Used for iteration 
        
    def insert(self, value: int) -> None:
        """Insert a value into the binary search tree."""
        self.root = self._insert(self.root, value)
        self.size += 1
    
    def _insert(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value <= node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node
    
    def search(self, value: int) -> bool:
        """Return True if the value is in the binary search tree, False otherwise."""
        return self._search(self.root, value)
    
    def _search(self, node: Optional[Node], value: int) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)
    
    def remove(self, value: int) -> None:
        """Remove a value from the binary search tree."""
        self.root = self._remove(self.root, value)
        self.size -= 1
    
    def _remove(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)
        return node
    
    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _max_value_node(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def _next_larger(self, node: Node, value: int) -> Optional[Node]:
        if node is None:
            return None
        
        if value < node.value:
            left_larger_node = self._next_larger(node.left, value)
            if left_larger_node is None:
                return node
            
            return left_larger_node
        
        return self._next_larger(node.right, value)
    
            
    def __str__(self) -> str:
        return str([value for value in self])
    
    def __contains__(self, value: int) -> bool:
        return self.search(value)
    
    def __len__(self) -> int:
        return self.size
    
    def __iter__(self):
        self._current = self._min_value_node(self.root)
        return self
    
    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._next_larger(self.root, value)
        return value
    

if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(4)
    binary_tree.insert(6)
    
    print("len: ", len(binary_tree))  # 6
    for value in binary_tree:
        print(value, end=" ") # 2 3 4 5 6 7
    print()
    
    print(3 in binary_tree)  # True
    print(8 in binary_tree)  # False
    
    binary_tree.remove(3)
    print("len: ", len(binary_tree))  # 5
    print(3 in binary_tree)  # False
    print(binary_tree)  # [2, 4, 5, 6, 7]