class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.idxMap = {}
    
    def add(self, n: int) -> None:
        idx = len(self.heap)
        self.heap.append(n)
        if n not in self.idxMap:
            self.idxMap[n] = set()
        self.idxMap[n].add(idx)
        self.swim(n)
    
    def remove(self, n: int) -> None:
        idx = self.idxMap[n][-1]
        self.removeAt(idx)
    
    def removeAt(self, idx: int) -> int:
        if idx >= len(self.heap):
            return -1
        tailIdx = len(self.heap) - 1
        valToRemove = self.heap[idx]

        self.swap(idx, tailIdx)
        self.heap.pop()
        self.idxMap[valToRemove].remove(tailIdx)
        if len(self.idxMap[valToRemove]) == 0:
            del self.idxMap[valToRemove]

        val = self.heap[idx]
        self.sink(idx)

        if val == self.heap[idx]:
            self.swim(idx)
        
        return valToRemove
        
    
    def swim(self, idx: int) -> None:
        parent = (idx - 1) // 2
        while idx > 0 and parent > 0 and self.heap[parent] > self.heap[idx]:
            self.swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2
        return

    def sink(self, idx: int) -> None:
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if left >= len(self.heap) or self.heap[smallest] >= self.heap[idx]:
                break
            
            self.swap(smallest, idx)
            idx = smallest

    def swap(self, idx1: int, idx2: int) -> None:
        val1 = self.heap[idx1]
        val2 = self.heap[idx2]

        self.heap[idx1] = val1
        self.heap[idx2] = val2

        self.idxMap[val1].remove(idx1)
        self.idxMap[val2].remove(idx2)

        self.idxMap[val1].add(idx2)
        self.idxMap[val2].add(idx1)

    
    def peek(self) -> int:
        if self.heap:
            return self.heap[0]
        return -1
    
    def poll(self) -> int:
        return self.removeAt(0)
    
    def contains(self, n: int) -> bool:
        return n in self.idxMap