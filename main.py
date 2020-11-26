# Fut trader app
import time
import pyautogui as pg
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# Accessing open browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

time.sleep(5)

#Button and mouse movement things
def move_mouse(x, y, sec):
    pg.moveTo(x + 10, y + 100, sec)


def click_back_button(movement_time):
    back_button = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
    move_mouse(back_button.location.get("x"), back_button.location.get("y"), movement_time)
    pg.click()
    print("Back button clicked")


def increase_min_bid_price(movement_time):
    time.sleep(0.5)
    try:
        min_bid_price_plus = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]")
        move_mouse(min_bid_price_plus.location.get("x"), min_bid_price_plus.location.get("y"), movement_time)
        pg.click()
        print("Min bid price clicked")
    except NoSuchElementException:
        click_back_button(2)


def click_search(movement_time):
    search_button = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
    move_mouse(search_button.location.get("x"), search_button.location.get("y"), movement_time)
    pg.click()
    print("Search clicked")


def snipe_player(snipe_time):
    time.sleep(0.15)
    try:
        print("Trying to snipe player")
        buy_now = driver.find_element_by_class_name("buyButton")
        move_mouse(buy_now.location.get("x"), buy_now.location.get("y"), snipe_time)
        pg.click()
        print("Snipe clicked")
        time.sleep(0.15)
        pg.keyDown("enter")
        pg.keyUp("enter")
        print("enter pushed")
        time.sleep(1.33)
        print("sleep waited try to list")
        list_sniped_player("1100", "1400")
    except NoSuchElementException:
        print("Snipe not successful")
        click_back_button(0.9)


def check_result():
    try:
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div[2]/div/span")
        click_back_button(0.7)
    except NoSuchElementException:
        print("Result found")
        snipe_player(0.11)

def reset_min_bid_price():
    bid_price_field = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input")
    move_mouse(bid_price_field.location.get("x"), bid_price_field.location.get("y"), 1)
    pg.click()
    pg.write("0")

# send_to_transfer_list = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]")
#LIST PLAYER
def list_sniped_player(min_price, buy_now):
    print("Try to list")
    try:
        driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[1]/div[2]/div/span[1]")
        click_list_on_transfer_market()
        set_min_price(min_price)
        set_buy_now_price(buy_now)
        list_player()
        print("player listed")
        click_back_button(1)
    except NoSuchElementException:
        print("cant list item")
        click_back_button(2)


def click_list_on_transfer_market():
    list_on_transfer_market = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")
    move_mouse(list_on_transfer_market.location.get("x"), list_on_transfer_market.location.get("y"), 1.3)
    pg.click()
    time.sleep(0.71)


def set_min_price(min_price):
    listing_min_price = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
    move_mouse(listing_min_price.location.get("x"), listing_min_price.location.get("y"), 0.8)
    pg.click()
    pg.write(min_price, interval=0.27)
    time.sleep(0.2)


def set_buy_now_price(buy_now):
    listing_buy_now_price = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
    move_mouse(listing_buy_now_price.location.get("x"), listing_buy_now_price.location.get("y"), 0.46)
    pg.click()
    pg.write(buy_now, interval=0.24)
    time.sleep(0.31)


def list_player():
    list_on_transfer_market_button = driver.find_element_by_xpath(
        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button")
    move_mouse(list_on_transfer_market_button.location.get("x"), list_on_transfer_market_button.location.get("y"),
               0.3)
    pg.click()

# TODO: open browser with a button: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
# TODO: Windowed application to set up things


# Processes
def search():
    increase_min_bid_price(0.5)
    click_search(0.4)

def try_to_buy_player(times):
    for i in range(0, times):
        search()
        check_result()
        if i % 8 == 0:
            reset_min_bid_price()

try_to_buy_player(20)
