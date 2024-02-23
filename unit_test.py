import unittest
from Floyd import floyd_warshall_recursive

class TestFloydWarshallRecursive(unittest.TestCase):
    def test_shortest_distances(self):
        graph = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0],
        ]
        expected_distances = [
            [0, 7, 12, 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0],
        ]
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected_distances)

if __name__ == '__main__':
    unittest.main()
