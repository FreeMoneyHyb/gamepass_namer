import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

# open the file with the list of alts
with open('alts.txt', 'r') as f:
    lines = f.readlines()

# loop through each line in the file
for line in lines:
    # split the line into email and password
    email, password = line.strip().split(':')
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # create a new Chrome browser instance
    driver = webdriver.Chrome()
    driver.get('https://www.minecraft.net/en-us/login')

    # fill in the email input field
    sign_in_button = driver.find_element(By.XPATH, '//a[@data-aem-contentname="Sign in with "]')
    sign_in_button.click()
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.element_to_be_clickable((By.ID, 'i0116')))
    email_input.send_keys(email)
    next_button = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
    next_button.click()

    # fill in the password input field
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'i0118')))
    time.sleep(1)
    password_input.send_keys(password)

    # click the "Sign in" button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"]')))
    sign_in_button.click()

    # click the "Yes" button
    yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"][@value="Yes"]')))
    yes_button.click()

    # click the "Profile Name" link
    profile_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-aem-contentname="Profile Name"]')))
    profile_link.click()

    # wait for the profile name input field to be clickable and type "popbob"
    profile_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="profile-name-input"]')))
    profile_input.clear()
    profile_input.send_keys(f'HUB{random_string}')

    # click the "Set Profile Name" button
    set_profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="ChangeNameButton"]')))
    set_profile_button.click()

    time.sleep(3)

    # close the browser
    driver.quit()