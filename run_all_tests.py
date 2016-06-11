import unittest
import test.test_testdialog as test_testdialog
import test.test_extractor as test_extractor

# all test suites
suite1 = test_testdialog.suite()
suite2 = test_extractor.suite()
all_tests = unittest.TestSuite((suite1, suite2))

my_test_runner = unittest.TextTestRunner()
my_test_runner.run(all_tests)
