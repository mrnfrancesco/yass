import unittest
import importlib

class TestRequirements(unittest.TestCase):
    def test_colorama(self):
        try:
            colorama = importlib.import_module('colorama')
        except ImportError:
            colorama = None

        self.assertIsNotNone(colorama, "Missing colorama mandatory requirement")

    def test_pyquery(self):
        try:
            pyquery = importlib.import_module('pyquery')
            # Missing __version__ in pyquery. Look at issue #107
            # self.assertGreaterEqual(pyquery.__version__, '1.2.9', "PyQuery >= 1.2.9 required")
        except ImportError:
            pyquery = None

        self.assertIsNotNone(pyquery, "Missing PyQuery mandatory requirement")


if __name__ == '__main__':
    unittest.main()