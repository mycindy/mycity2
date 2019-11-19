# coding=utf-8
import unittest

# # assert 的用法

class IntegerArithmeticTestCase(unittest.TestCase):
    def test_1(self):
        '''用例说明：1111'''
        print("111111")
        a="admin"
        b="admin1"
        self.assertTrue(a!=b)
        # self.assertTrue(a==b)
        # self.assertTrue(a in b)
        # self.assertTrue(a not in b)
        #
        # self.assertEqual(a,b)
        # self.assertNotEqual(a,b)
        #
        # self.assertIn(a,b)
        # self.assertNotIn(a,b)
        #
        # self.assertIsNone(x)     # 判断是否为空 x is None          
        # self.assertIsNotNone(x)  # 判断是否为空  x is not None


    @classmethod
    def setUpClass(cls):
        print("用例前，只执行一次")
    @classmethod
    def tearDownClass(cls):
        print("用例后，只调用一次")

    # def setUp(self):
    #     #每个用例执行之前都执行一次
    #     print("先打开浏览器")
    #
    # def tearDown(self):
    #     #每个用例执行完之后，调用一次
    #     print("关闭浏览器")


