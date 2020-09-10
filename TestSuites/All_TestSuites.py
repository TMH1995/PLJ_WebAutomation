import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner

from AutomatingTestScripts.VerifyLoginScenarios import LoginTest
from AutomatingTestScripts.VerifyResetScenarios import resetTest

#Get all the tests from LoginTest, S
TS1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TS2=unittest.TestLoader().loadTestsFromTestCase(resetTest)

#Creating test suites
FunctionalTestSuite=unittest.TestSuite([TS1,TS2]) #Functional test suite

runner= HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_name="Full Report PLJ",output = r'C:\Users\\TARIQ\\PycharmProjects\\PLJ_WebAutomation\\Reports')
runner.run(FunctionalTestSuite)