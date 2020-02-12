class min_heap:
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
            if self.heap[parent_index].weight <= self.heap[current_index].weight:
                break
            self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
            current_index = parent_index

    def pop(self):
        if len(self.heap) == 0:
            return None
        temp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]

        current_index = 0
        while(True):
            if current_index == len(self.heap) - 1:
                break

            right_index = (current_index * 2) + 2
            if self.heap[right_index].weight < self.heap[current_index].weight:
                self.heap[right_index], self.heap[current_index] = self.heap[current_index], self.heap[right_index]
                current_index = right_index
                continue

            left_index = (current_index * 2) + 1
            if self.heap[left_index].weight < self.heap[current_index].weight:
                self.heap[left_index], self.heap[current_index] = self.heap[current_index], self.heap[left_index]
                current_index = left_index
                continue

            break

        return temp

    def print(self):
        print(self.heap)

class node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.neighbors = []

    def add_neighbor(name):
        self.neighbors.append(name)

    def __repr__(self):
        return self.name + " - " + str(self.weight)

class graph:
    def __init__(self, edge_weight):
        nodes = set()
        for key in edge_weight:
            nodes |= set(key)
        print(edge_weight)
        print(nodes)

g = graph({
    ("A", "B"): 3,
    ("A", "C"): 1,
    ("B", "C"): 7,
    ("B", "D"): 5,
    ("B", "E"): 1,
    ("C", "D"): 2,
    ("D", "E"): 7,
})

#g.start("A", "E")

h = min_heap()
h.push(node("A", 20))
h.push(node("B", 10))
h.push(node("C", 50))
h.push(node("D", 40))
h.push(node("E", 45))
h.push(node("F", 60))
h.push(node("G", 5))
h.print()
temp = h.pop()
print(temp)
h.print()