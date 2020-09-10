from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://eduplj.com/")

driver.find_element_by_xpath("//*[@id='login-details']/div/a[1]/div/div[2]").click()
time.sleep(2)
driver.find_element_by_id("teacher_c").clear()
driver.find_element_by_id("teacher_c").send_keys("1")
driver.implicitly_wait(3)
driver.find_element_by_id("teacher_p").clear()
driver.find_element_by_id("teacher_p").send_keys("1")
driver.find_element_by_id("response").click()
driver.implicitly_wait(3)
errorMessage="Please lengthen this text to 8 characters or more (you are currently using 1 character)."
message=driver.find_element_by_id("teacher_p").get_attribute("validationMessage")
print(message)
if(errorMessage==message):
    print("Test passed")
else:
    print("Test failed")
driver.quit()