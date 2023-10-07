# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

# Other imports
import time
from getpass import getpass
import os
import sys

# Constants
ZEBRA_PORTAL_URL = "https://portal.zebrarobotics.com/"
ZEBRA_LMS_URL = "https://lms.zebrarobotics.com"
COURSES = [
    'C620',
    'C820',
    'C840',
    'R420',
    'R440',
    'R460',
    'R520',
    'R620',
    'R640',
    'R660'
]
# Getting passwords from environment variables
USER = os.getenv('USER')
PORTAL_PASS = os.getenv('PORTAL_PASS')
CANVAS_PASS = os.getenv('CANVAS_PASS')

# Setting cmd or control, depending on operating system
cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL


def open_new_tab_to_url(driver, url):
    ''' The open_new_tab function takes the WebDriver and a URL
        to open as parameters. It opens a new tab, not a new
        window, going to the specified URL.
    '''
    # Creates a new tab and navigates to URL
    driver.execute_script(
        f'window.open("{url}", "new_window")')
    # Switches window focus to our new window
    driver.switch_to.window(driver.window_handles[1])


def portal_login(driver):
    ''' The portal_login function takes our WebDriver object as a 
    parameter and logs into the Zebra Robotics portal.
    '''

    # Opens the Zebra Robotics Login Page
    driver.get(ZEBRA_PORTAL_URL)

    # Enters username and password, then clicks submit button
    driver.find_element(By.NAME, 'email').send_keys(USER)
    driver.find_element(By.NAME, 'password').send_keys(PORTAL_PASS)
    driver.find_element(By.ID, 'kt_login_signin_submit').click()

    # Selects the branch
    driver.find_element(By.ID, 'kt_subheader_quick_actions').click()
    driver.find_element(By.LINK_TEXT, 'Cary').click()

    # Saves the window ID for ZR portal
    # portal_window_id = chrome_driver.current_window_handle


def canvas_login(driver):
    ''' The canvas_login function takes our WebDriver object as a parameter and logs into the Zebra Robotics Canvas.
    '''
    # LMS Login Credentials
    # lms_username = input("LMS Username: ")
    # lms_password = getpass("LMS Password: ")

    # Open a new tab going to Canvas
    open_new_tab_to_url(driver, ZEBRA_LMS_URL)

    # Enters username and password into LMS, then clicks submit
    driver.find_element(
        By.CSS_SELECTOR, '#pseudonym_session_unique_id').send_keys(USER)
    driver.find_element(
        By.XPATH, '//*[@id="pseudonym_session_password"]').send_keys(CANVAS_PASS)
    driver.find_element(
        By.CSS_SELECTOR, '#login_form > div.ic-Login__actions > div.ic-Form-control.ic-Form-control--login > button').click()


def find_attendance(driver):
    ''' The find_attendance function will open the attendance,
    navigate to the correct day, and open the correct batch of 
    students.
    '''
    # TODO
    driver.find_element(
        By.XPATH, '//*[@id="kt_header_menu"]/ul/li[2]/a').click()
    driver.find_element(
        By.XPATH, '//*[@id="kt_header_menu"]/ul/li[2]/div/ul/li[1]/a').click()


def open_link_in_new_tab(driver, link_text):
    ''' The open_link_in_new_tab function takes the driver and the link text as
        parameters, and cmd clicks to open the link as a new tab.
    '''
    link = driver.find_element(By.PARTIAL_LINK_TEXT, link_text)
    ActionChains(driver).key_down(cmd_ctrl).click(
        link).perform()


def main():
    # Chrome Options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("incognito")

    # Currently Testing
    # chrome_options.add_experimental_option("detach", True)

    # Chrome WebDriver
    chrome_driver = webdriver.Chrome(options=chrome_options)

    # Setting page login delay
    chrome_driver.implicitly_wait(5)

    # Minimizes the window until further input
    # chrome_driver.minimize_window()

    # Logs into Zebra Dashboard
    portal_login(chrome_driver)

    # find_attendance(chrome_driver)

    # Logs into Zebra Canvas LMS
    canvas_login(chrome_driver)

    # chrome_driver.find_element(By.PARTIAL_LINK_TEXT, 'Courses').click()
    for link in COURSES:
        open_link_in_new_tab(chrome_driver, link)

    # TEMPORARY
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
