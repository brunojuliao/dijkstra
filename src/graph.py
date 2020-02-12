from math import inf
from .min_heap import MinHeap
from .node import Node
import copy

class Graph:
    def __init__(self, edge_cost):
        self.edge_cost = edge_cost

        self.node_names = set()
        self.remaining = MinHeap()
        self.previous = []
        self.nodes = dict()
        for key in edge_cost:
            self.node_names |= set(key)

            if key[0] not in self.nodes:
                self.nodes[key[0]] = Node(key[0], inf)
            self.nodes[key[0]].add_neighbor(key[1])

            if key[1] not in self.nodes:
                self.nodes[key[1]] = Node(key[1], inf)
            self.nodes[key[1]].add_neighbor(key[0])

    def find_shortest_path(self, start_node_name, end_node_name):
        self.previous = []
        nodes = copy.deepcopy(self.nodes)
        start_node = nodes[start_node_name]
        start_node.cost = 0
        self.remaining.push(start_node)

        while True:
            node = self.remaining.pop()

            if node is None:
                break

            self.visit(node, nodes)

            if node.name == end_node_name:
                break

        print(self.previous)

    def visit(self, node, nodes):
        node.is_visited = True
        self.previous.append(node.name)

        neighbor_heap = MinHeap()

        for neighbor_name in node.neighbors:
            neighbor_node = nodes[neighbor_name]

            if neighbor_node.is_visited:
                continue

            if (node.name, neighbor_name) in self.edge_cost:
                cost = node.cost + self.edge_cost[(node.name, neighbor_name)]
            elif (neighbor_name, node.name) in self.edge_cost:
                cost = node.cost + self.edge_cost[(neighbor_name, node.name)]
            
            if cost < neighbor_node.cost:
                neighbor_node.cost = cost
                neighbor_heap.push(neighbor_node)
        
        min_neighbor = neighbor_heap.pop()
        if min_neighbor != None:
            self.remaining.push(min_neighbor)


g = Graph({
    ("A", "B"): 3,
    ("A", "C"): 1,
    ("B", "C"): 7,
    ("B", "D"): 5,
    ("B", "E"): 1,
    ("C", "D"): 2,
    ("D", "E"): 7,
})

g.find_shortest_path("A", "E")
g.find_shortest_path("C", "B")