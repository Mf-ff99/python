# Selenium Web Scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # use keyboard inputs
import time

# chromedriver runs from its specified location
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("insert website here")

search = driver.find_element_by_id("s")
search.send_keys("test search")
search.send_keys(Keys.RETURN)

time.sleep(6)


driver.quit()