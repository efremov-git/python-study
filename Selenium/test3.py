from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link ="http://joyreactor.cc/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

