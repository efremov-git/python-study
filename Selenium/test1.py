from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://avito.ru"
browser = webdriver.Chrome()
browser.get(link)

search_string = browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input")
search_string.send_keys("Капибара")

button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/button/span")
button.click()
time.sleep(5)

check = browser.find_element(By.XPATH,
                             "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input").text
check2 = "Капибара"
if check == check2:
    print("test passed")
else:
    print("test failed")
browser.quit()
