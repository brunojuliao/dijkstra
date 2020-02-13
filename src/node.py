class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.neighbors = []
        self.is_visited = False

    def add_neighbor(self, name):
        self.neighbors.append(name)

    def is_less_than(self, other_node):
        if self.cost > other_node.cost:
            return False
        return True

    def __repr__(self):
        return self.name + " - " + str(self.cost)