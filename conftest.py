from pytest import fixture
from time import sleep
from selenium import webdriver
@fixture
def set_tear():
    driver=webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    sleep(10)
    yield driver
    driver.quit()

