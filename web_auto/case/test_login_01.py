# coding=utf-8
import unittest
from selenium import webdriver
import time

class LoginTest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1:8000/index/")
        self.is_alert_exist()
        self.driver.delete_all_cookies() #清空cooks 退出登录
        self.driver.refresh()
        #self.driver=webdriver.Firefox() #加self 局部变量driver变成全局变量



    def get_login_username(self):
        try:
            t=self.driver.find_element_by_xpath(".//*[@id='navbar']/ul[2]/li[1]/a").text
            print(t)
            return t
        except:
            return ""
    def is_alert_exist(self):
        ##p判断alert是否存在
        try:
            time.sleep(2)
            alert=self.driver.switch_to.alert
            text=alert.text
            alert.accept()
            return text
        except:
            return ""

    def login(self,user,psw):
        self.driver.find_element_by_name("username").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("btn").click()

    def test_01(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.login("admin","123456")
        #判断是否登录成功
        time.sleep(1)
        t=self.get_login_username()
        print("获取的结果:%s"%t)
        self.assertTrue(t=="admin1")

    def test_02(self):
        '''登录失败的案例'''
        time.sleep(2)
        ##错误账号和密码
        self.login("admin1","123456")
        time.sleep(1)
        t=self.get_login_username()
        print("登录失败，获取结果:%s"%t)
        self.assertTrue(t=="")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()



