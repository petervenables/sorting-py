import unittest
import simple_sort

class TestSimpleSortMethods(unittest.TestCase):

    def test_empty_list(self):
        result = simple_sort.sort([])
        self.assertTrue(len(result) == 0)

    def test_singleton_list(self):
        result = simple_sort.sort(["a"])
        self.assertTrue(len(result) == 1)

    def test_sort(self):
        result = simple_sort.sort(["b","a"])
        self.assertEqual(result, ["a","b"])

    def test_sort_words(self):
        result = simple_sort.sort(["rabbit", "dog", "mouse", "cat"])
        self.assertEqual(result, ["cat", "dog", "mouse", "rabbit"])

    def test_sort_mixed_case(self):
        result = simple_sort.sort(["ampersand", "Ampersand"])
        self.assertEqual(result, ["Ampersand", "ampersand"])

    def test_buried_duplicate(self):
        result = simple_sort.sort(["A", "B", "C", "A", "B"])
        self.assertEqual(result, ["A", "A", "B", "B", "C"])


if __name__ == '__main__':
    unittest.main()