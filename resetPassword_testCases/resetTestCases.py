import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class reset ():
    def resetWithValidCredentials(self,driver):
        Status=False
        driver.get("https://eduplj.com/")
        driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
        time.sleep(2)
        driver.find_element_by_class_name("reset-password-link").click()
        time.sleep(2)
        driver.find_element_by_id("code").send_keys("110110")
        driver.find_element_by_id("email").send_keys("test@tyahoo.com")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/div[3]/div/button").click()
        time.sleep(2)
        confirmationMessage = "We have e-mailed your password reset link, note that the link is valid for 24 hours only."
        message = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div").get_attribute("innerHTML")
        message = message.strip()
        if confirmationMessage==message:
            Status =True
            print("The test passed and the message displayed was "+"'"+confirmationMessage+"'")
        else:
            print("The test failed and the message displayed is " + message +"Which is not as the designed message "+ confirmationMessage)
        return Status

    def resetWithInvalidCredentials(self,driver):
        Status=False
        driver.get("https://eduplj.com/")
        driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
        time.sleep(2)
        driver.find_element_by_class_name("reset-password-link").click()
        time.sleep(2)
        driver.find_element_by_id("code").send_keys("110110")
        driver.find_element_by_id("email").send_keys("t123@tyahoo.com")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/div[3]/div/button").click()
        time.sleep(2)
        errorMessage = "Teacher code or email is invalid."
        message = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/span/strong").get_attribute(
            "innerHTML")
        message = message.strip()
        if errorMessage==message:
            Status=True
            print("The test passed and the message displayed was "+"'"+errorMessage+"'")
        else:
            print("The  message displayed is " + "'"+message+"'" +"Which is not as the designed message "+ "'"+errorMessage+"'")
        return Status