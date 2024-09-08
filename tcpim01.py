from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Set up the WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

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

# Click on 'Add Employee'
add_employee_button = driver.find_element(By.ID, "menu_pim_addEmployee")
add_employee_button.click()

# Fill in the employee details
first_name = driver.find_element(By.ID, "firstName")
middle_name = driver.find_element(By.ID, "middleName")
last_name = driver.find_element(By.ID, "lastName")
employee_id = driver.find_element(By.ID, "employeeId")

first_name.send_keys("John")
middle_name.send_keys("A")
last_name.send_keys("Doe")
employee_id.clear()
employee_id.send_keys("12345")

# Optionally, create login details for the new employee
create_login_details_checkbox = driver.find_element(By.ID, "chkLogin")
create_login_details_checkbox.click()

username = driver.find_element(By.ID, "user_name")
password = driver.find_element(By.ID, "user_password")
confirm_password = driver.find_element(By.ID, "re_password")
status = driver.find_element(By.ID, "status")

username.send_keys("john.doe")
password.send_keys("password123")
confirm_password.send_keys("password123")
status.send_keys("Enabled")

# Save the new employee
save_button = driver.find_element(By.ID, "btnSave")
save_button.click()

# Wait for a few seconds to see the result
time.sleep(3)

# Close the browser
driver.quit()
