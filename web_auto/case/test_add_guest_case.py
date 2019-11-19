from  selenium import webdriver
from pages.login_page2 import LoginPage
from  pages.add_guest_page import AddGuestPage
import unittest
import time
#addguest="http://127.0.0.1:8000/admin/sign/guest/add/"

class AddGuestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.fbh=AddGuestPage(cls.driver)
        a=LoginPage(cls.driver)
        a.login()

    def setUp(self):
        #每个用例都在一个起点
        self.driver.get("http://127.0.0.1:8000/admin/")


    def test_add_guest(self):
        '''添加guest'''
        timestr=time.strftime("%S")
        name="xioawang"+timestr
        phone="12345"+timestr
        mail=name+"@mail.com"
        self.fbh.add_guest(name,phone,mail)
        result=self.fbh.is_add_success(name)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=="__main__":
    unittest.main()