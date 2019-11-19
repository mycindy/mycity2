# coding: utf-8
import  unittest

from common import HTMLTestRunner_cn

casePath="C:\\Users\\RENJINFENG\\PycharmProjects\\web_auto\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath="C:\\Users\\RENJINFENG\\PycharmProjects\\web_auto\\report\\"+"result.html"

fp=open(reportPath,"wb") #wb 二进制方式写入

runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                        title="报告的title",
                                        description='用例执行情况',
                                        retry=1)

runner.run(discover)
fp.close()