from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class LoginValid():
    def LoginWithValidCredentials(self,driver):
        Status=False
        driver.get("https://eduplj.com/")

        driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
        time.sleep(2)
        driver.find_element_by_id("teacher_c").clear()
        driver.find_element_by_id("teacher_c").send_keys("110110")
        driver.implicitly_wait(3)
        driver.find_element_by_id("teacher_p").clear()
        driver.find_element_by_id("teacher_p").send_keys("123456789")
        driver.find_element_by_id("response").click()
        delay = 3 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'image-template')))
            Status=True
            print("The test passed and PLJ Dashboard was opened successfully")
        except TimeoutException:
            print("The test failed due to a problem while loading the Dashboard")
            return Status
        return Status

    def LoginWithInvalidCredentials(self,driver):
        driver.get("https://eduplj.com/")

        driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
        time.sleep(2)
        driver.find_element_by_id("teacher_c").clear()
        driver.find_element_by_id("teacher_c").send_keys("11101110")
        driver.implicitly_wait(3)
        driver.find_element_by_id("teacher_p").clear()
        driver.find_element_by_id("teacher_p").send_keys("11111111111111")
        driver.find_element_by_id("response").click()
        driver.implicitly_wait(3)
        errorMessage = "These credentials do not match our records"
        invalidLoginMessage = driver.find_element_by_id("tech_c").get_attribute("innerHTML")
        invalidLoginMessage = invalidLoginMessage.strip()
        status = False
        if (errorMessage == invalidLoginMessage):
            status = True
            print("The test passed and the error message displayed is "+"'"+errorMessage+"'")
        else:
            print("The test failed and the error message displayed is " + "'"+invalidLoginMessage +"'"+"Which is not as the designed message "+ "'"+errorMessage+"'")
        return status

    def LoginWithInvalidPasswordLengthConstraint(self,driver):
        driver.get("https://eduplj.com/")
        status = False
        driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
        time.sleep(2)
        driver.find_element_by_id("teacher_c").clear()
        driver.find_element_by_id("teacher_c").send_keys("1")
        driver.implicitly_wait(3)
        driver.find_element_by_id("teacher_p").clear()
        driver.find_element_by_id("teacher_p").send_keys("1")
        driver.find_element_by_id("response").click()
        driver.implicitly_wait(3)
        errorMessage = "Please lengthen this text to 8 characters or more (you are currently using 1 character)."
        message = driver.find_element_by_id("teacher_p").get_attribute("validationMessage")
        if (errorMessage == message):
            status = True
            print("The test passed and the error message displayed is " + "'"+errorMessage+"'")
        else:
            print("The test failed and the error message displayed is " +"'"+ message +"Which is not as the designed message "+"'" +errorMessage+"'")

        return status