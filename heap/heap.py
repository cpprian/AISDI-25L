class DHeap:
    def __init__(self, _d):
        self.d = _d
        self.heap = []

    def parent(self, i):
        return (i - 1) // self.d

    def children(self, i):
        children = []
        for j in range(self.d):
            child_index = self.d * i + j + 1
            if child_index < len(self.heap):
                children.append(child_index)
        return children

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
            self.heapify_down(0)
        return top

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def heapify_down(self, i):
        while True:
            children = self.children(i)

            if not children:
                break

            min_child = min(children, key=lambda x: self.heap[x])
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break

    def display(self):
        if not self.heap:
            print("Heap is empty.")
            return

        index = 0
        level = 0
        count = 1
        while index < len(self.heap):
            next_index = index + count
            print("Level", level, ":", self.heap[index:next_index])
            index = next_index
            count *= self.d
            level += 1
