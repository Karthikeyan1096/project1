from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Set up the WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximize the browser window
driver.maximize_window()

# Find the username and password fields and enter the credentials
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
username.send_keys("Admin")
password.send_keys("admin123")

# Click the login button
login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()

# Wait for a few seconds to see the result
time.sleep(20)

# Close the browser
driver.quit()
