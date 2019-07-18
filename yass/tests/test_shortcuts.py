import unittest
from yass.plugins import Aol

from yass.shortcuts import iter_plugins


class TestShortcuts(unittest.TestCase):
    def test_iter_plugins(self):

        # Check with False predicate
        self.assertListEqual(list(), iter_plugins(lambda cls: False))

        # Check True and None predicate equality
        self.assertListEqual(
            iter_plugins(None),
            iter_plugins(lambda cls: True)
        )

        # Check non-emptyness of True/None predicate
        self.assertGreater(len(iter_plugins(None)), 0)

        # Check plugin existance
        self.assertIn(Aol, iter_plugins(None))

        # Check No-Aol predicate
        self.assertNotIn(Aol, iter_plugins(lambda cls: cls is not Aol))
