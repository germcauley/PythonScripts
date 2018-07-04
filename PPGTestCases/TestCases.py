import unittest
import HTMLTestRunner
import os
from LifeMomentsNavigation import Life_Moments_Navigation

#run all tests, write to a html report file
dir = os.getcwd()

LM_test = unittest.TestLoader().loadTestsFromTestCase(Life_Moments_Navigation)



test_suite = unittest.TestSuite(LM_test)

outfile = open(dir + "\TestResults.html", "w")


runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

runner.run(test_suite)