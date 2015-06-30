import unittest
import inspect
import sys

import test_shortcuts
import test_requirements
import test_helpers

if __name__ == '__main__':
    def suite(module):
        """
        Create and return a *unittest.TestSuite* from test methods in the specified module

        :param module: the module to look for test case
        :type module: module
        :return: a preconfigured *unittest.TestSuite* with all test methods in specified module
        :rtype: unittest.TestSuite
        """
        test_suite = list()

        # Take all the members in `module` which are children classes of `unittest.TestCase`
        test_cases = inspect.getmembers(
            module,
            lambda cls: inspect.isclass(cls) and (unittest.TestCase in inspect.getmro(cls))
        )
        # Iterate over TestCase classes to get test methods (those whose name starts with "test_")
        for _, test_case in test_cases:
            test_methods = inspect.getmembers(
                test_case,
                lambda m: inspect.ismethod(m) and m.__name__.startswith('test_')
            )
            # Create a TestSuite which contains all the test methods for the given test case
            test_suite.append(unittest.TestSuite(map(test_case, [test_method for test_method, _ in test_methods])))

        # Return the mother of the test suite
        return unittest.TestSuite(test_suite)

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.TestSuite([
            suite(test_helpers),
            suite(test_requirements),
            suite(test_shortcuts),
        ])
    )

    if result.failures:
        sys.exit(1)  # make Travis CI to fail in case of errors
    else:
        sys.exit(0)