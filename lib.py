from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
def wait_until(func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        locator=args[1]
        w=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locator)
        w.until(v)
        func(*args,**kwargs)
    return wrapper
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    @wait_until
    def enter_text(self,locator,/,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait_until
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
