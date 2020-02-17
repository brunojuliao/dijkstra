from src.node import Node

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        self.heap.append(node)
        current_index = len(self.heap) - 1
        while(current_index > 0):
            offset = 2 if current_index % 2 == 0 else 1
            parent_index = int((current_index - offset) / 2)
            if self.heap[parent_index].is_less_than(self.heap[current_index]):
                break
            self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
            current_index = parent_index

    def pop(self):
        heap_length = len(self.heap)
        if heap_length == 0:
            return None
        elif heap_length == 1:
            return self.heap.pop()

        node = self.heap.pop(0)
        self.heap.insert(0, self.heap.pop())
        heap_length = len(self.heap)

        current_index = 0
        while(heap_length > 1 and current_index < heap_length - 1):
            right_index = (current_index * 2) + 2
            if right_index < heap_length and self.heap[right_index].is_less_than(self.heap[current_index]):
                self.heap[right_index], self.heap[current_index] = self.heap[current_index], self.heap[right_index]
                current_index = right_index
                continue

            left_index = (current_index * 2) + 1
            if left_index < heap_length and self.heap[left_index].is_less_than(self.heap[current_index]):
                self.heap[left_index], self.heap[current_index] = self.heap[current_index], self.heap[left_index]
                current_index = left_index
                continue

            break

        return node

    def print(self):
        print(self.heap)

    def get_repr(self):
        return self.heap.__repr__()