class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        self.heap.append(node)
        current_index = len(self.heap) - 1
        while(True):
            if current_index == 0:
                break
            offset = 2 if current_index % 2 == 0 else 1
            parent_index = int((current_index - offset) / 2)
            if self.heap[parent_index].is_less_than(self.heap[current_index]):
                break
            self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
            current_index = parent_index

    def pop(self):
        if len(self.heap) == 0:
            return None
        temp = self.heap[0]
        last_index = len(self.heap) - 1
        self.heap[0] = self.heap[last_index]

        del self.heap[last_index]

        current_index = 0
        while(True):
            if current_index == last_index:
                break

            right_index = (current_index * 2) + 2
            if right_index in self.heap and self.heap[right_index].is_less_than(self.heap[current_index]):
                self.heap[right_index], self.heap[current_index] = self.heap[current_index], self.heap[right_index]
                current_index = right_index
                continue

            left_index = (current_index * 2) + 1
            if left_index in self.heap and self.heap[left_index].is_less_than(self.heap[current_index]):
                self.heap[left_index], self.heap[current_index] = self.heap[current_index], self.heap[left_index]
                current_index = left_index
                continue

            break

        return temp

    def print(self):
        print(self.heap)

    def get_repr(self):
        return self.heap.__repr__()