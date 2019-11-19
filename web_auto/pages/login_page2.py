#coding utf-8
from selenium import webdriver
from common.base import Base
import time

login_url="http://127.0.0.1:8000/admin/"

class LoginPage(Base):

    #定位登录
    loc_user=("id","id_username")
    loc_psw=("id","id_password")
    loc_button=("xpath",".//*[@id='login-form']/div[3]/input")

    loc_get_user=("css selector","#user-tools>strong")

    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_psw(self,text=""):
        self.sendKeys(self.loc_psw,text)

    def click_login_button(self):
        self.click(self.loc_button)


    def get_login_name(self):
        user=self.get_text(self.loc_get_user)
        return user

    def get_login_result(self,user):
        result=self.is_text_in_element(self.loc_get_user,user)
        return result

    def is_alert_exist(self):
        ##p判断alert是否存在
        a=self.is_alert()
        if a:
            print(a.text)
            a.accept()


    # def is_refresh_exist(self):
    #     '''判断忘记密码页，刷新按钮，刷新按钮是否存在'''
    #     r=self.isElementExist(self.locator)
    #     return r


    def login(self,user="admin",psw="admin123456",keep_login=False):
        '''登录流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if keep_login:self.click_login_button()
        self.click_login_button()



if __name__=="__main__":
    driver=webdriver.Firefox()
    login_page=LoginPage(driver)
    login_page.login(keep_login=True)#不写参数，默认是False
    # driver.get(login_url)
    # login_page.input_user("admin")
    # login_page.input_psw("admin123456")
    # login_page.click_login_button()
    # login_page.get_login_name()


