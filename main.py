# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# Other imports
import time
from getpass import getpass

#Constants
ZEBRA_PORTAL_URL = "https://portal.zebrarobotics.com/"
ZEBRA_LMS_URL = "https://lms.zebrarobotics.com"

# The portal_login function takes our WebDriver object as a parameter
# and logs into the Zebra Robotics portal.
# @param driver - WebDriver object
def portal_login(driver):
    # Portal Login Credentials
    portal_username = input("Portal Username: ")
    portal_password = getpass("Portal Password: ")

    # Opens the Zebra Robotics Login Page
    driver.get(ZEBRA_PORTAL_URL)

    # Enters username and password, then clicks submit button
    driver.find_element(By.NAME, 'email').send_keys(portal_username)
    driver.find_element(By.NAME, 'password').send_keys(portal_password)
    driver.find_element(By.ID, 'kt_login_signin_submit').click()

    # Selects the branch
    driver.find_element(By.ID, 'kt_subheader_quick_actions').click()
    driver.find_element(By.LINK_TEXT, 'Cary').click()

    # Saves the window ID for ZR portal
    #portal_window_id = chrome_driver.current_window_handle

# The canvas_login function takes our WebDriver object as a parameter
# and logs into the Zebra Robotics Canvas.
# @param driver - WebDriver object
def canvas_login(driver):
    # LMS Login Credentials
    lms_username = input("LMS Username: ")
    lms_password = getpass("LMS Password: ")

    # Creates a new tab and navigates to Canvas
    driver.execute_script('window.open("https://lms.zebrarobotics.com", "new_window")')

    driver.switch_to.window(driver.window_handles[1])
    # Enters username and password into LMS, then clicks submit
    driver.find_element(By.CSS_SELECTOR, '#pseudonym_session_unique_id').send_keys(lms_username)
    driver.find_element(By.XPATH, '//*[@id="pseudonym_session_password"]').send_keys(lms_password)
    driver.find_element(By.CSS_SELECTOR, '#login_form > div.ic-Login__actions > div.ic-Form-control.ic-Form-control--login > button').click()


def main():
    # Chrome Options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("incognito")

    # Currently Testing
    #chrome_options.add_experimental_option("detach", True) 

    # Chrome WebDriver
    chrome_driver = webdriver.Chrome(options=chrome_options)

    # Setting page login delay
    chrome_driver.implicitly_wait(5)

    # Minimizes the window until further input
    #chrome_driver.minimize_window()

    # Logs into Zebra Dashboard
    portal_login(chrome_driver)

    # Logs into Zebra Canvas LMS
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
    main()