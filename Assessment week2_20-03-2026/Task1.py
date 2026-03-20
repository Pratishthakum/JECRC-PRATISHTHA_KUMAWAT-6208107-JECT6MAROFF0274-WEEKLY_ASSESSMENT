from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in')
driver.maximize_window()

wait_obj = WebDriverWait(driver, 10)
print("title of page is: ",driver.title)
print("current url: ",driver.current_url)

submit_button = wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-inner"]')))
submit_button.click()
dropdown_button = wait_obj.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
sleep(3)
select = Select(dropdown_button)
select.select_by_visible_text("Books")
sleep(3)
search01= wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search01.send_keys("Harry Potter", Keys.ENTER)
sleep(3)
Name_of_product = wait_obj.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-component-type="s-search-results"]/descendant::h2')))
print("\nFirst 5 Products displayed:")
for i in Name_of_product[:5]:
    print(i.text)

Name_of_product[0].click()

driver.quit()






