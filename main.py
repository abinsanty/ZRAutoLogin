# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# Other imports
import time
from getpass import getpass

# Login credentials
username = input("Username: ")
password = getpass("Password: ")

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("incognito")

# Currently Testing
#chrome_options.add_experimental_option("detach", True) 

# Chrome WebDriver
chrome_driver = webdriver.Chrome(options=chrome_options)

# Opens the Zebra Robotics Login Page
chrome_driver.get("https://portal.zebrarobotics.com/")

# Waiting for login page to load
chrome_driver.implicitly_wait(5)

# Enters username and password, then clicks submit button
chrome_driver.find_element(By.NAME, 'email').send_keys(username)
chrome_driver.find_element(By.NAME, 'password').send_keys(password)
chrome_driver.find_element(By.ID, 'kt_login_signin_submit').click()

# Selects the branch
chrome_driver.find_element(By.ID, 'kt_subheader_quick_actions').click()
chrome_driver.find_element(By.LINK_TEXT, 'Cary').click()

# Minimizes the window until further input
chrome_driver.minimize_window()

### TEMPORARY
# Keeps window open until user exits with Ctrl+C
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Closes the WebDriver manually
chrome_driver.quit()
