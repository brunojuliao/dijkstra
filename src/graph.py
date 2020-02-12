from math import inf
from .min_heap import MinHeap
from .node import Node

class Graph:
    def __init__(self, edge_weight):
        nodes = set()
        for key in edge_weight:
            nodes |= set(key)
        print(edge_weight)
        print(nodes)

g = Graph({
    ("A", "B"): 3,
    ("A", "C"): 1,
    ("B", "C"): 7,
    ("B", "D"): 5,
    ("B", "E"): 1,
    ("C", "D"): 2,
    ("D", "E"): 7,
})

#g.start("A", "E")