from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://eduplj.com/")

driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
time.sleep(2)
driver.find_element_by_class_name("reset-password-link").click()
time.sleep(2)
driver.find_element_by_id("code").send_keys("110110")
driver.find_element_by_id("email").send_keys("t123@tyahoo.com")
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/div[3]/div/button").click()
time.sleep(2)
errorMessage="Teacher code or email is invalid."
message=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/span/strong").get_attribute("innerHTML")
message=message.strip()
if errorMessage==message:
    print("Test passed")
else:
    print("Test failed")
driver.quit()