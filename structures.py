# Educational purposes

class Heap:
    def __init__(self, data):
        self.data = data 

    def insert(self):
        pass

    def extract(self):
        pass

    def max(self):
        return len(self.data)

    def max_heapify(self, i):
        node = self.data[i]
        left = self.data[i * 2 - 1] if i * 2 - 1 < self.max() else None
        right = self.data[i * 2] if i * 2 < self.max() else None
        if left or right:
            g_child = i * 2 - 1 if left > right else i * 2
            if node < self.data[g_child]:
                temp = self.data[g_child]
                self.data[i - 1] = temp
                self.max_heapify(g_child + 1)

    def build_max_heap(self):
        for i in range(self.max() / 2, i >= 1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        pass