# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# Other imports
import time
from getpass import getpass

#Constants
ZEBRA_PORTAL_URL = "https://portal.zebrarobotics.com/"
ZEBRA_LMS_URL = "https://lms.zebrarobotics.com"

# TODO
# Need to learn **kwargs and *args
def create_chrome_webdriver():
    pass

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("incognito")

# Currently Testing
#chrome_options.add_experimental_option("detach", True) 

# Chrome WebDriver
chrome_driver = webdriver.Chrome(options=chrome_options)

def portal_login(driver):
    # Portal Login Credentials
    portal_username = "***REMOVED***" #input("Portal Username: ")
    portal_password = "***REMOVED***" #getpass("Portal Password: ")

    # Opens the Zebra Robotics Login Page
    driver.get(ZEBRA_PORTAL_URL)

    # Waiting for login page to load
    driver.implicitly_wait(5)

    # Enters username and password, then clicks submit button
    driver.find_element(By.NAME, 'email').send_keys(portal_username)
    driver.find_element(By.NAME, 'password').send_keys(portal_password)
    driver.find_element(By.ID, 'kt_login_signin_submit').click()

    # Selects the branch
    driver.find_element(By.ID, 'kt_subheader_quick_actions').click()
    driver.find_element(By.LINK_TEXT, 'Cary').click()

    # Saves the window ID for ZR portal
    portal_window_id = chrome_driver.current_window_handle

def canvas_login(driver):
    # LMS Login Credentials
    lms_username = "***REMOVED***" #input("LMS Username: ")
    lms_password = "***REMOVED***" #getpass("LMS Password: ")

    # Creates a new tab and navigates to Canvas
    driver.execute_script('window.open("https://lms.zebrarobotics.com", "new_window")')

    #chrome_driver.switch_to.window('Log In to Canvas')

    #driver.get(ZEBRA_LMS_URL)

    # Enters username and password into LMS, then clicks submit
    driver.find_element(By.NAME, 'pseudonym_session[unique_id]').send_keys(lms_username)
    driver.find_element(By.ID, 'pseudonym_session[password]').send_keys(lms_password)
    driver.find_element(By.TAG_NAME, 'button').click()

# Minimizes the window until further input
#chrome_driver.minimize_window()
portal_login(chrome_driver)

#chrome_driver.execute_script('window.open("https://lms.zebrarobotics.com", "new_window")')

#chrome_driver.switch_to.new_window('tab')

canvas_login(chrome_driver)

### TEMPORARY
# Keeps window open until user exits with Ctrl+C
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Closes the WebDriver manually
chrome_driver.quit()

if __name__ == '__main__':
    pass
