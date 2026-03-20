from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get(" https://the-internet.herokuapp.com/login")
driver.maximize_window()
element1=driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print(element1)
element2=driver.find_element(By.CSS_SELECTOR,'input[id="password"]')
print(element2)
element3=driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print(element3)

element4 = driver.find_element(By.CSS_SELECTOR,'div[class="footer"] a')
print(element4)


sleep(5)
driver.quit()