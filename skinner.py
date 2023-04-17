import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Huys Stop Skidding My Code FR FR https://cdn.discordapp.com/attachments/1097578571649794208/1097580502426329168/image.png
with open('alts.txt', 'r') as f:
    lines = f.readlines()


for line in lines:
    driver = webdriver.Chrome()
    folder_path = os.path.join(os.getcwd(), "skins")
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    file_name = random.choice(file_list)
    file_path = os.path.join(folder_path, file_name)
    try:
        email, password = line.strip().split(':')
        driver.get('https://www.minecraft.net/en-us/login')
        sign_in_button = driver.find_element(By.XPATH, '//a[@data-aem-contentname="Sign in with "]')
        sign_in_button.click()
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.element_to_be_clickable((By.ID, 'i0116')))
        email_input.send_keys(email)
        next_button = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
        next_button.click()
        password_input = wait.until(EC.element_to_be_clickable((By.ID, 'i0118')))
        time.sleep(1)
        password_input.send_keys(password)
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"]')))
        sign_in_button.click()
        time.sleep(2)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"][@value="Yes"]')))
        yes_button.click()
        profile_skin = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-aem-contentname="Change Skin"]')))
        profile_skin.click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='classic']")))
        element.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        element = driver.find_element(By.XPATH, '//input[@type="file"]')
        element.send_keys(file_path)
        upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-aem-contentname="Upload"]')))
        upload_button.click()
        time.sleep(2)
        driver.quit()
    except Exception as e:
        print(f"ERROR: {e}")
