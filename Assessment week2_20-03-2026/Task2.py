

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://automationexercise.com')

wait=WebDriverWait(driver,6)
signup_button=wait.until(ec.element_to_be_clickable((By.XPATH,'//a[text()=" Signup / Login"]')))
signup_button.click()

Name=wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@data-qa='signup-name']")))
Name.send_keys('prati')

email=wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@data-qa='signup-email']")))
email.send_keys('pratishtha40240@gmail.com')

submit_button=wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Signup']")))
submit_button.click()

gender_radio=wait.until(ec.element_to_be_clickable((By.ID,'id_gender2')))
gender_radio.click()

password=wait.until(ec.element_to_be_clickable((By.ID,'password')))
password.send_keys('8767676767')

checkboxes=wait.until(ec.presence_of_all_elements_located((By.XPATH,'//input[@type="checkbox"]')))
for checkbox in checkboxes:
    checkbox.click()
    checkbox.get_attribute('checked')

