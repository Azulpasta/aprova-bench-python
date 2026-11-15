#!/usr/bin/env python3
import unittest
import sys

# Import the test module
from tree_building_test import TreeBuildingTest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TreeBuildingTest)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
