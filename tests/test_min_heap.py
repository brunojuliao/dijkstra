import unittest
from src.node import Node
from src.min_heap import MinHeap

class test_min_heap(unittest.TestCase):
    def setUp(self):
        self.min_node = Node("G", 5)

        self.test_heap = MinHeap()
        self.test_heap.push(Node("A", 20))
        self.test_heap.push(Node("B", 10))
        self.test_heap.push(Node("C", 50))
        self.test_heap.push(Node("D", 40))
        self.test_heap.push(Node("E", 45))
        self.test_heap.push(Node("F", 60))
        self.test_heap.push(self.min_node)

    def test_min_heap_order(self):
        #Arrange
        repr_to_compare = "[G - 5, A - 20, B - 10, D - 40, E - 45, F - 60, C - 50]"

        #Act
        #Assert
        self.assertEqual(self.test_heap.get_repr(), repr_to_compare)

    def test_min_heap_min(self):
        #Arrange
        #Act
        temp = self.test_heap.pop()
        #Assert
        temp = self.min_node

if __name__ == '__main__':
    unittest.main()