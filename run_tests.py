#!/usr/bin/env python3
import unittest
import sys

# Import the test class
from list_ops_test import ListOpsTest

if __name__ == '__main__':
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ListOpsTest)

    # Run the tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with status code
    sys.exit(0 if result.wasSuccessful() else 1)
