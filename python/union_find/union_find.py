class UnionFind:
    def __init__(self, size: int):
        # Size of total elements
        self.size = size

        # Track size of each group
        self.size_dict = {}

        # Track ids
        self.id = {}

        for i in range(size):
            self.size[i] = 1
            self.id[i] = i

    def union_find():
        pass

    def find(self, p: int) -> int:
        root = p
        while root != self.id[root]:
            root = self.id[root]
        
        # Path compression
        # Only compress for nodes that have been used
        self.id[p] = root
        return root
    
    def unify(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)

        sizeP = self.size_dict[rootP]
        sizeQ = self.size_dict[rootQ]

        if sizeP >= sizeQ:
            self.id[rootQ] = rootP
            self.size_dict[rootP] += sizeQ
            del self.size_dict[rootQ]
        else:
            self.id[rootP] = rootQ
            self.size_dict[rootQ] += sizeP
            del self.size_dict[rootP]
    
    def isConnected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)
    