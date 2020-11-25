# Fut trader app
import time
import pyautogui as pg
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# Accessing open browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Change chrome driver path accordingly
chrome_driver = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
time.sleep(5)


def move_mouse(x, y, sec):
    pg.moveTo(x + 10, y + 100, sec)


def click_back_button(movement_time):
    back_button = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
    move_mouse(back_button.location.get("x"), back_button.location.get("y"), movement_time)
    pg.click()


def increase_min_bid_price(movement_time):
    min_bid_price_plus = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div["
                                                      "1]/div[2]/div[2]/div[2]/button[2]")
    move_mouse(min_bid_price_plus.location.get("x"), min_bid_price_plus.location.get("y"), movement_time)
    pg.click()


def click_search(movement_time):
    search_button = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
    move_mouse(search_button.location.get("x"), search_button.location.get("y"), movement_time)
    pg.click()


def snipe_player(snipe_time):
    buy_now = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
    move_mouse(buy_now.location.get("x"), buy_now.location.get("y"), snipe_time)
    pg.click()
    time.sleep(0.25)
    pg.keyDown("enter")
    pg.keyUp("enter")


def check_result():
    try:
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]/div/span")
        click_back_button(1.3)
    except NoSuchElementException:
        snipe_player(0.5)


# send_to_transfer_list = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]")

def list_sniped_player(min_price, buy_now):
    try:
        driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[1]/div[2]/div/span[1]")
        click_list_on_transfer_market()
        set_min_price(min_price)
        set_buy_now_price(buy_now)
        list_player()
    except NoSuchElementException:
        click_back_button(2)


def click_list_on_transfer_market():
    list_on_transfer_market = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")
    move_mouse(list_on_transfer_market.location.get("x"), list_on_transfer_market.location.get("y"), 1.3)
    pg.click()
    time.sleep(3)

def set_min_price(min_price):
    listing_min_price = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
    move_mouse(listing_min_price.location.get("x"), listing_min_price.location.get("y"), 1.17)
    pg.click()
    pg.write(min_price, interval=0.27)
    time.sleep(1.45)

def set_buy_now_price(buy_now):
    listing_buy_now_price = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
    move_mouse(listing_buy_now_price.location.get("x"), listing_buy_now_price.location.get("y"), 1.26)
    pg.click()
    pg.write(buy_now, interval=0.24)
    time.sleep(1.67)

def list_player():
    list_on_transfer_market_button = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button")
    move_mouse(list_on_transfer_market_button.location.get("x"), list_on_transfer_market_button.location.get("y"),
               1.10)
    pg.click()
    click_back_button(2)
