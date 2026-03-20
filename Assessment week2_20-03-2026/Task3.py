'''
## Task 3

### Automation script for google.com

'''


# ## Task 3
#
# ### Automation script for google.com
#
# Open Google
#
# Enter "Selenium Python"
#
# Use explicit wait for suggestions
#
# Capture all suggestions using find_elements
#
# Print them
#
# Click one suggestion


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


# from unicodedata import category

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.google.com/")
driver.maximize_window()

wait=WebDriverWait(driver,5)
search=wait.until(EC.presence_of_element_located((By.XPATH,'//textarea[@id="APjFqb"]')))
search.send_keys('Selenium Python')

all_suggestion=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="Alh6id"]/descendant::div[@class="wM6W7d"]/span')))

for s in all_suggestion:
    print(s.text)

suggestion02=wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[@id="Alh6id"]/descendant::div[@class="wM6W7d"]/span)[2]')))
suggestion02.click()


driver.quit()