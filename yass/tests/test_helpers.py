import unittest

from yass.helpers import without_duplicates


class TestHelpers(unittest.TestCase):
    def test_without_duplicates(self):
        no_duplicates = [1, 2, 3, 4, 5]
        duplicated = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

        # Test non iterable objects
        self.assertRaises(TypeError, without_duplicates, None)
        self.assertRaises(TypeError, without_duplicates, 'a string')
        self.assertRaises(TypeError, without_duplicates, 3)
        self.assertRaises(TypeError, without_duplicates, 3.14)

        # Test default empty iterables
        self.assertListEqual(list(), without_duplicates(list()))
        self.assertSetEqual(set(), without_duplicates(set()))
        self.assertTupleEqual(tuple(), without_duplicates(tuple()))

        # Test default iterables with no duplicated items
        self.assertListEqual(no_duplicates, without_duplicates(no_duplicates))
        self.assertSetEqual(set(no_duplicates), without_duplicates(set(no_duplicates)))
        self.assertTupleEqual(tuple(no_duplicates), without_duplicates(tuple(no_duplicates)))

        # Test default iterables with duplicated items
        self.assertListEqual(no_duplicates, without_duplicates(duplicated))
        self.assertSetEqual(set(no_duplicates), without_duplicates(set(duplicated)))
        self.assertTupleEqual(tuple(no_duplicates), without_duplicates(tuple(duplicated)))
