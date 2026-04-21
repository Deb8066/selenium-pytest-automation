import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Text fields
driver.find_element(By.ID, "name").send_keys("Test Name")
driver.find_element(By.ID, "email").send_keys("testemail@xyz.com")
driver.find_element(By.ID, "phone").send_keys("2244567890")

#Radio Button
driver.find_element(By.ID, "male").click()

#Check Box
driver.find_element(By.XPATH, "//input[@id='sunday']").click()

#Country dropdown
Select(driver.find_element(By.ID, "country")).select_by_index(1)

#Color Drop Down
Select(driver.find_element(By.ID, "colors")).select_by_value("blue")

# Date picker
driver.find_element(By.ID, "datepicker").send_keys("05/25/1987")
driver.find_element(By.ID, "start-date").send_keys("03/25/2026")
driver.find_element(By.ID, "end-date").send_keys("04/21/2026")

# Submit
driver.find_element(By.XPATH, "//button[@class='submit-btn']").click()

# Result validation
result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
assert result == "You selected a range of 27 days."


driver.quit()