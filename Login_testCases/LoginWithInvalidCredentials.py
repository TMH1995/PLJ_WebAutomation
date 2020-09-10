from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe")
driver.maximize_window()
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
errorMessage="These credentials do not match our records"
invalidLoginMessage=driver.find_element_by_id("tech_c").get_attribute("innerHTML")
invalidLoginMessage=invalidLoginMessage.strip()
if(errorMessage==invalidLoginMessage):
    print("Test passed")
else:
    print("Test failed")
driver.quit()