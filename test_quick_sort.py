import unittest
import quick_sort as qs

class TestQuickSort(unittest.TestCase):

    unsorted = ["D", "C", "J", "X", "P", "K", "A", "M", "W", "B"]
    sorted = ["A", "B", "C", "D", "J", "K", "M", "P", "W", "X"]

    def test_sort_ok(self):
        result = qs.sort(self.unsorted)
        self.assertEqual(result, self.sorted)

    def test_sort_length(self):
        result = qs.sort(self.unsorted)
        self.assertEqual(len(result), len(self.unsorted))

if __name__ == '__main__':
    unittest.main()

