"""
## Union Find

### Description
Union Find is a data structure that keeps track of elements which are partitioned into disjoint sets.
It uses path compression and union by rank to optimize the operations
(the amortized time complexity is O(α(n)), where α(n) is the inverse Ackermann function).
It supports two operations:
- Find: Determine which set a particular element is in. It returns an element from that set that serves as its "representative".
- Union: Join two sets into a single set.

### Operations
- find(x: int) -> int: Return the representative of the set containing x.
- union(x: int, y: int) -> None: Join the sets containing x and y.

### Example
```python
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
print(uf.find(0))  # 2
print(uf.find(1))  # 2
print(uf.find(2))  # 2
print(uf.find(3))  # 4
print(uf.find(4))  # 4
```
"""


class UnionFind:
    """A class representing a Union Find data structure."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            self.parent[x_root] = y_root
            

if __name__ == "__main__":
    UnionFind(5)
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print(uf.find(0))  # 2
    print(uf.find(1))  # 2
    print(uf.find(2))  # 2
    print(uf.find(3))  # 4
    
    uf.union(0, 4)
    print(uf.find(0))  # 4
    print(uf.find(1))  # 4
    print(uf.find(2))  # 4
    print(uf.find(3))  # 4
    print(uf.find(4))  # 4
    
