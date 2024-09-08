from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximize the browser window
driver.maximize_window()

# Log in to the OrangeHRM portal
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
username.send_keys("Admin")
password.send_keys("admin123")
login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()

# Wait for the dashboard to load
time.sleep(3)

# Navigate to the PIM module
pim_module = driver.find_element(By.ID, "menu_pim_viewPimModule")
pim_module.click()

# Search for the employee by name or ID
employee_name = "John Doe"  # Replace with the actual employee name or ID
search_name_field = driver.find_element(By.ID, "empsearch_employee_name_empName")
search_name_field.send_keys(employee_name)
search_button = driver.find_element(By.ID, "searchBtn")
search_button.click()

# Wait for the search results to load
time.sleep(3)

# Click on the employee name to edit
employee_link = driver.find_element(By.LINK_TEXT, employee_name)
employee_link.click()

# Wait for the employee details page to load
time.sleep(3)

# Edit the employee details
first_name = driver.find_element(By.ID, "personal_txtEmpFirstName")
first_name.clear()
first_name.send_keys("John Updated")

# Save the changes
save_button = driver.find_element(By.ID, "btnSave")
save_button.click()

# Wait for a few seconds to see the result
time.sleep(3)

# Close the browser
driver.quit()
