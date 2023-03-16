from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link ="https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.get(link)

search_string = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input")
search_string.send_keys("Капибара")

button = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button")
button.click()
time.sleep(5)

check = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-search/rz-catalog/div/div[1]/rz-search-heading/div/h1").text
check2 = "Капибара"
if check == check2:
    print("test passed")
else:
    print("test failed")
browser.quit()