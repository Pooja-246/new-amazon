from lib import SeleniumWrapper
class RegisterPage:
    _lnk_register=("link text","Register")
    _rdo_male=("id", "gender-male")
    _rdo_female=("id", "gender-female")
    _txt_firstname=("id","FirstName")
    _txt_lastname=("id","LastName")
    _txt_email=("id","Email")
    _txt_password=("id","Password")
    _txt_confirmpass=("id","ConfirmPassword")
    _btn_register=("id","register-button")
    def __init__(self,driver):
        self.driver=driver
    def register(self,gender,fname,lname,email,password):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(RegisterPage._lnk_register)
        if gender.upper()=="MALE":
            sw.click_element(RegisterPage._rdo_male)
        elif gender.upper()=="FEMALE":
            sw.click_element(RegisterPage._rdo_female)
        sw.enter_text(RegisterPage._txt_firstname,value=fname)
        sw.enter_text(RegisterPage._txt_lastname,value=lname)
        sw.enter_text(RegisterPage._txt_email,value=email)
        sw.enter_text(RegisterPage._txt_password,value=password)
        sw.enter_text(RegisterPage._txt_confirmpass,value=password)
        sw.click_element(RegisterPage._btn_register)