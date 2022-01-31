import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://www.amatis.nl/")

driver.maximize_window()

time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/section[4]/div[3]/div/a")
element.click()

time.sleep(5)

element = driver.find_element(By.XPATH, "/html/body/section/div[3]/ul/li[3]/a/span[2]/span[4]")
element.click()

time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[1]/div[2]/a[4]")
element.click()

time.sleep(5)
element = driver.find_element(By.LINK_TEXT, "BLOG")
element.click()

time.sleep(5)
element = driver.find_element(By.LINK_TEXT, "LinkedIn")
element.click()

time.sleep(20)
driver.close()





