import unittest

import pkg_resources


class TestRequirements(unittest.TestCase):
    def test_requirements(self):
        # Check colorama requirement
        pkg_resources.require('colorama')

        # Check pyquery requirement and version
        pyquery_version = pkg_resources.require('pyquery')[0].version
        major, minor, micro = pyquery_version.split('.')
        self.assertTrue(
            major > 1  # version 2 or greater
            or (major == 1 and minor > 2)  # version 1.3 or greater
            or (major == 1 and minor == 2 and micro >= 9),  # version 1.2.9 or greater
            "PyQuery version MUST be >= 1.2.9 (got {version} instead)".format(version=pyquery_version)
        )


if __name__ == '__main__':
    unittest.main()
