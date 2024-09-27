"""
## summary:
The module contains classes that represent a map (dictionary).

## classes:
- Entry: A class representing a key-value pair.
- Node: A class representing a node in a binary search tree.
- Dictionary: A class representing a map (dictionary) by using binary search trees.
"""


from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Entry:
    """A class representing a key-value pair."""
    key: Any
    value: Any


class Node:
    """A class representing a node in a binary search tree."""

    def __init__(self, entry: Entry):
        self.entry = entry
        self.left = None
        self.right = None


class Map:
    """A class representing a map (dictionary)."""
    
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __getitem__(self, key: Any) -> Any:
        return self._get(self.root, key)
    
    def _get(self, node: Optional[Node], key: Any) -> Any:
        if node is None:
            raise KeyError(key)
        if key == node.entry.key:
            return node.entry.value
        if key < node.entry.key:
            return self._get(node.left, key)
        return self._get(node.right, key)
    
    def __setitem__(self, key: Any, value: Any) -> None:
        self.root = self._set(self.root, Entry(key, value))
    
    def _set(self, node: Optional[Node], entry: Entry) -> Node:
        if node is None:
            self.size += 1
            return Node(entry)
        if entry.key == node.entry.key:
            node.entry = entry
        elif entry.key < node.entry.key:
            node.left = self._set(node.left, entry)
        else:
            node.right = self._set(node.right, entry)
        return node
    
    def __contains__(self, key: Any) -> bool:
        return self._contains(self.root, key)
    
    def _contains(self, node: Optional[Node], key: Any) -> bool:
        if node is None:
            return False
        if key == node.entry.key:
            return True
        if key < node.entry.key:
            return self._contains(node.left, key)
        return self._contains(node.right, key)
    
    def __delitem__(self, key: Any) -> None:
        self.root = self._delete(self.root, key)
        self.size -= 1
    
    def _delete(self, node: Optional[Node], key: Any) -> Node:
        if node is None:
            raise KeyError(key)
        if key == node.entry.key:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_node = self._min(node.right)
            node.entry = min_node.entry
            node.right = self._delete(node.right, min_node.entry.key)
        elif key < node.entry.key:
            node.left = self._delete(node.left, key)
        else:
            node.right = self._delete(node.right, key)
        return node
    
    def _min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node
    
    def __iter__(self):
        return self._inorder(self.root)
    
    def _inorder(self, node: Optional[Node]):
        if node is not None:
            yield from self._inorder(node.left)
            yield node.entry.key
            yield from self._inorder(node.right)
            
    def items(self):
        return ((key, self[key]) for key in self)
    
    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {self[key]}" for key in self) + "}"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)})"


if __name__ == "__main__":
    d = Map()
    d[1] = "one"
    d[2] = "two"
    d[3] = "three"
    print(d)
    del d[2]
    print(d)
    print(1 in d)
    print(2 in d)
    print(3 in d)
    print(4 in d)
    print(len(d))
    print(d[1])
    print(d[3])
    
    d[1] = "ONE"
    d[3] = "THREE"
    
    for key in d:
        print(key)
    
    for key, value in d.items():
        print(key, value)