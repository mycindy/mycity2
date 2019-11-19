#coding utf-8
from selenium import webdriver
from common.base import Base

class AddGuestPage(Base):
    #添加Guest
    loc_add=("xpath",".//*[@id='content-main']/div[2]/table/tbody/tr[2]/td[1]/a")
    loc_event=("xpath",".//*[@id='id_event']/option[5]")
    loc_realname=("id","id_realname")
    loc_phone=("id","id_phone")
    loc_email=("id","id_email")
    loc_save=("xpath",".//*[@id='guest_form']/div/div/input[1]")

    #判断
    loc_NAME=("xpath",".//*[@id='result_list']/tbody/tr[1]/th/a")


    def add_guest(self,realname,phone,email):
        self.click(self.loc_add)
        self.click(self.loc_event)
        self.sendKeys(self.loc_realname,realname)
        self.sendKeys(self.loc_phone,phone)
        self.sendKeys(self.loc_email,email)
        self.click(self.loc_save)

    def is_add_success(self,text):
        return self.is_text_in_element(self.loc_NAME,text)

if __name__=="__main__":
    driver=webdriver.Firefox()
    fbh=AddGuestPage(driver)

    from pages.login_page2 import LoginPage
    a=LoginPage(driver)
    a.login()


    fbh.add_guest("xiaolv","132568","xiaolv@mail.com")
    result=fbh.is_add_success("xiaolv")
    print(result)

