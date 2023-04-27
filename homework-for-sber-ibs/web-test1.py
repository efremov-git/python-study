import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://reqres.in/")

upgrade_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section[8]/button")
upgrade_button.click()


emailpanel = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section[8]"
                                                    "/div/div/form/div/div[1]/input")
emailpanel.send_keys("test@test")

subscribe_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section[8]/div/div/form/div/div["
                                                          "4]/input")
subscribe_button.click()
time.sleep(10)

driver.quit()
