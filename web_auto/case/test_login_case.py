'''
1.输入admin,输入admin123456 点击登录
2.输入admin，输入 点击登录
3.输入 ，输入admin123456 点击登录
'''
from selenium import webdriver
import unittest
from pages.login_page2 import LoginPage, login_url

class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies() #清空cooks 退出登录
        self.driver.refresh()


    def test_01(self):
        '''输入admin,输入admin123456 点击登录'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("admin123456")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="ADMIN")

    def test_02(self):
        '''输入admin，输入 点击登录'''
        self.loginp.input_user("admin")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="")

    def test_03(self):
        '''输入 ，输入admin123456 点击登录'''
        self.loginp.input_psw("admin123456")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="main":
    unittest.main()