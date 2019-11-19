#coding utf-8
from selenium import webdriver
from common.base import Base

class Login(Base):

    #定位登录
    loc1=("id","id_username")
    loc2=("id","id_password")
    loc3=("xpath",".//*[@id='login-form']/div[3]/input")


    def login(self,user="admin",psw="admin123456"):
        #self.driver.get("http://127.0.0.1:8000/admin/")
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        self.click(self.loc3)