from time import sleep
from lib import SeleniumWrapper
class LoginPage:
    _lnk_login=("link text","Log in")
    _txt_email=("id","Email")
    _txt_password=("id","Password")
    _btn_login=("xpath","//input[@class='button-1 login-button']")
    def __init__(self,driver):
        self.driver=driver
    def login(self,email,password):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(LoginPage._lnk_login)
        sw.enter_text(LoginPage._txt_email,value=email)
        sw.enter_text(LoginPage._txt_password,value=password)
        sw.click_element(LoginPage._btn_login)
    def is_displayed_email(self,email):
        _xpath=f"//a[text()='{email}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath",_xpath).is_displayed()
            except Exception:
                sleep(1)
                continue
        return False
