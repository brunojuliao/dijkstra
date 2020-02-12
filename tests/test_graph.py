import unittest
from src.node import Node
from src.min_heap import MinHeap
from src.graph import Graph

class test_graph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph({
            ("A", "B"): 3,
            ("A", "C"): 1,
            ("B", "C"): 7,
            ("B", "D"): 5,
            ("B", "E"): 1,
            ("C", "D"): 2,
            ("D", "E"): 7,
        })

    def test_scenario1(self):
        #Arrange
        expected = "[A - 0, C - 1, D - 3, E - 10]"
        #Act
        result = self.graph.find_shortest_path("A", "E")
        #Assert
        self.assertEqual(expected, result.__repr__())

    def test_scenario2(self):
        #Arrange
        expected = "[C - 0, A - 1, B - 4]"
        #Act
        result = self.graph.find_shortest_path("C", "B")
        #Assert
        self.assertEqual(expected, result.__repr__())

    def test_both(self):
        #Arrange
        expected1 = "[A - 0, C - 1, D - 3, E - 10]"
        expected2 = "[C - 0, A - 1, B - 4]"
        #Act
        result1 = self.graph.find_shortest_path("A", "E")
        result2 = self.graph.find_shortest_path("C", "B")
        #Assert
        self.assertEqual(expected1, result1.__repr__())
        self.assertEqual(expected2, result2.__repr__())