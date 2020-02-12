class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.neighbors = []

    def add_neighbor(name):
        self.neighbors.append(name)

    def __repr__(self):
        return self.name + " - " + str(self.weight)