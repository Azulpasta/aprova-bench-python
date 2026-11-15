#!/usr/bin/env python3

import sys
import unittest

# Run the tests
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('dominoes_test')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
