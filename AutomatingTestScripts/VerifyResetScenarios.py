import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

from resetPassword_testCases.resetTestCases import reset
test = reset()

class resetTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        global driver
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe",chrome_options=options)
        # driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe")
        # driver.implicitly_wait(10)
        # driver.maximize_window()

    @classmethod
    def tearDown(self):
        driver.delete_all_cookies()
        driver.close()
        driver.quit()

    def test_resetWithValidCredentials(self):
        Status=test.resetWithValidCredentials(driver)
        self.assertEqual(True, Status, "TestCase Fails")

    def test_resetWithInvalidCredentials(self):
        Status=test.resetWithInvalidCredentials(driver)
        self.assertEqual(True, Status, "TestCase Fails")


if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\\TARIQ\\PycharmProjects\\PLJ_WebAutomation\\Reports'))
