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
driver.find_element_by_id("email").send_keys("test@tyahoo.com")
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/form/div[3]/div/button").click()
time.sleep(2)
confirmationMessage="We have e-mailed your password reset link, note that the link is valid for 24 hours only."
message=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div").get_attribute("innerHTML")
message=message.strip()
if confirmationMessage==message:
    print("Test passed")
else:
    print("Test failed")

driver.quit()