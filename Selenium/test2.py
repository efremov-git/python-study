import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link ="http://joyreactor.cc/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.ID, "s")
search_string.send_keys("Капибара")

button = browser.find_element(By.ID, "searchsubmit").click()


check = browser.find_element(By.TAG_NAME, "h1").text
check2 = "Капибара"

if check == check2:
    print("test passed")
else:
    print("test failed")
browser.quit()