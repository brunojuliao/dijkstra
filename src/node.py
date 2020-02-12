class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.neighbors = []
        self.is_visited = False

    def add_neighbor(self, name):
        self.neighbors.append(name)

    def __repr__(self):
        return self.name + " - " + str(self.cost)