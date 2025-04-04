class Heap:
    def __init__(self, _d):
        self.d = _d
        self.heap = []

    def parent(self, i):
        return (i - 1) // self.d

    def children(self, i):
        return [self.d * i + j + 1 for j in range(self.d) if self.d * i + j + 1 < len(self.heap)]
    
    def append(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapify_down
        return top

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = i - 1

    def heapify_down(self, i):
        while True:
            children = self.children(i)

            if not children:
                break

            min_child = min(children, key=lambda x: self.heap(x))
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break