import sys
sys.path.append('../')
from sys import maxsize
NO_PATH = maxsize
import unittest
import test_cases

from recursion.recursive_floyd_done import FW, FWmain
GRAPH = []  # Initialize GRAPH as an empty list or with a default value


def FW():
    v = len(GRAPH)
    dist = [row[:] for row in GRAPH]  # Create a deep copy of the graph

    # Recursive function to compute shortest paths
    def RE(i, j, k):
        if k < 0:
            return dist[i][j]  # Base case: no intermediate vertices
        without_k = RE(i, j, k - 1)
        with_k = (RE(i, k, k - 1) + RE(k, j, k - 1)) if (
                    RE(i, k, k - 1) != NO_PATH and RE(k, j, k - 1) != NO_PATH) else NO_PATH
        return min(with_k, without_k)

    # Update the distance matrix using the recursive function
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = RE(i, j, k)

    return dist

class TestRecursion(unittest.TestCase):
    def test_case_0(self):
        global GRAPH
        GRAPH = test_cases.test0  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected0)

    def test_case_1(self):
        global GRAPH
        GRAPH = test_cases.test1  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected1)  # Ensure you compare with expected1

    def test_case_2(self):
        global GRAPH
        GRAPH = test_cases.test2  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected2)

    def test_case_3(self):
        global GRAPH
        GRAPH = test_cases.test3  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected3)

    def test_case_4(self):
        global GRAPH
        GRAPH = test_cases.test4  # Set the global GRAPH variable
        result = FW()
        self.assertError(result)

    def test_case_5(self):
        global GRAPH
        GRAPH = test_cases.test5  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected5)

    def test_case_6(self):
        global GRAPH
        GRAPH = test_cases.test6  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected6)

    def test_case_7(self):
        global GRAPH
        GRAPH = test_cases.test7  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected7)

    def test_case_8(self):
        global GRAPH
        GRAPH = test_cases.test8  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected8)

    def test_case_9(self):
        global GRAPH
        GRAPH = test_cases.test9  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected9)

    def test_case_10(self):
        global GRAPH
        GRAPH = test_cases.test10  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected10)

    def test_case_11(self):
        global GRAPH
        GRAPH = test_cases.test11  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected11)

    def test_case_12(self):
        global GRAPH
        GRAPH = test_cases.test12  # Set the global GRAPH variable
        result = FW()
        self.assertError(result)

    def test_case_13(self):
        global GRAPH
        GRAPH = test_cases.test13  # Set the global GRAPH variable
        result = FW()
        self.assertEqual(result, test_cases.expected13)
if __name__ == '__main__':
    unittest.main()


