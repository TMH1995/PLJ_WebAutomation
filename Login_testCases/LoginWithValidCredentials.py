
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException




driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\Chrome_driver\chromedriver.exe")
driver.maximize_window()
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
    print("Test passed")
except TimeoutException:
    print("Test failed")
driver.quit()

