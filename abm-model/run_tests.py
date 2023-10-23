import os
import sys
import unittest

def run_unit_tests():
    """
    Runs unit tests (without subprocesses).
    """
    tests = os.path.join(os.path.dirname(__file__)),
                         'abm-model', 'tests')
    suite = unittest.defaultTestLoader.discover(tests, pattern='test*.py')
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if res.wasSuccessful() else 1)
