import time
import random
import string
import random_word
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open the file with the list of alts
with open('alts.txt', 'r') as f:
    lines = f.readlines()

abbreviations = ['YT', 'XD', '_']  # only keep YT, XD, and _ in the list

# loop through each line in the file
for line in lines:
    driver = webdriver.Chrome()
    try:
        email, password = line.strip().split(':')
        ok = random.randint(2, 3)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=ok))
        driver.get('https://www.minecraft.net/en-us/login')
        word = random_word.RandomWords().get_random_word()
        if random.random() < 0.05:
            word = random.choice(['_', 'x']) + word
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
        try:
            skip_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="iShowSkip"]')))
            skip_link.click()
            try:
                get_it_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="iNext"]')))
                get_it_now_button.click()
            except:
                pass
        except:
            pass
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"][@value="Yes"]')))
        yes_button.click()
        try:
            skip_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="iShowSkip"]')))
            skip_link.click()
            try:
                get_it_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="iNext"]')))
                get_it_now_button.click()
            except:
                pass
        except:
            pass
        profile_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-aem-contentname="Profile Name"]')))
        profile_link.click()
        profile_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="profile-name-input"]')))
        rand_num = random.random()
        if rand_num < 0.45:
            profile_name = f'{word}{random_string}'
        elif rand_num < 0.9:
            profile_name = f'{word}{random.randint(100, 999)}'
        else:
            profile_name = f'{word}{random.choice(abbreviations) if random.random() < 0.1 else ""}'  # Add abbreviations with a 10% probability

        profile_input.clear()
        profile_input.send_keys(profile_name)

        set_profile_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="ChangeNameButton"]')))
        set_profile_button.click()
        time.sleep(3)
        driver.quit()
    except Exception as e:
        print(f"ERROR: {e}")
        driver.quit()
