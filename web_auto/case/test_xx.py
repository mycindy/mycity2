'''
1.输入admin,输入admin123456 点击登录
2.输入admin，输入 点击登录
3.输入admin1 ，输入admin123456 点击登录
'''
from selenium import webdriver
import unittest
from pages.login_page2 import LoginPage, login_url
import ddt
from common.read_excel import ExcelUtil
import os

##测试的数据
testdatas=[{"user":"admin","psw":"admin123456","expect": True},
           {"user":"admin","psw":"","expect": False},
           {"user":"admin1","psw":"admin123456","expect": False}]

# propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#
# filepath=os.path.join(propath,"common","datas.xlsx")
# print(filepath)
# data = ExcelUtil(filepath)
# testdatas=data.dict_data()
# print(testdatas)


@ddt.ddt
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


    def login_case(self,user,psw,expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        result=self.loginp.get_login_result("ADMIN")
        print("测试结果：%s"%result)
        self.assertTrue(result==expect)


    @ddt.data(*testdatas)
    def test_01(self,data):
        '''输入admin,输入admin123456 点击登录'''
        print("-----------------开始测试------------------")
        print("测试数据:%s"%data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("----------------结束：pass！----------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="main":
    unittest.main()