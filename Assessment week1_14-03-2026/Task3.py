from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()


websites = [
    "https://www.thesouledstore.com/",
    "https://www.nike.com/",
    "https://www.amazon.in/",
    "https://www.bbc.com/",
    "https://www.python.org/"
]


for site in websites:
    sleep(3)
    driver.get(site)
    print("Title of page:", driver.title)


sleep(3)


driver.quit()