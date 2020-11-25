#Fut trader app
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
time.sleep(5)

def click_back_button():
    back_button = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
    pg.moveTo(back_button.location.get("x") + 10, back_button.location.get("y") + 100, 3)
    pg.click()
