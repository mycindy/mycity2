import time
import unittest
from selenium import webdriver
from pages.add_guest_page import AddGuestPage
from pages.login_page import Login


class Test_add_guest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.fbh1=AddGuestPage(cls.driver)
        cls.fbh2=Login(cls.driver)
        cls.driver.get("http://127.0.0.1:8000/admin/")
        cls.fbh2.login()

    #def setUp(self):
        #self.driver=webdriver.Firefox() #加self 局部变量driver变成全局变量


    def test_add_guest(self):
        timestr=time.strftime("%S")
        name="xioawang"+timestr
        phone="12345"+timestr
        mail=name+"@mail.com"
        self.fbh1.add_guest(name,phone,mail)
        result=self.fbh1.is_add_success(name)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()