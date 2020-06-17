from Common.Logger import Log
from Common.ReadExcel import ReadExcel
import requests
import unittest
import json
import re


class Login(unittest.TestCase):
    def setUp(self) -> None:
        Log().info("执行测试用例")

    def tearDown(self) -> None:
        Log().info("执行完毕")

    def test_case01(self):
        """
        正常登陆
        """
        self.url = ReadExcel().excel_content(2, 3)
        self.data = ReadExcel().excel_content(2, 6)
        request_data = json.loads(self.data)
        response = requests.post(url=self.url, data=request_data)
        result = re.findall(r">注销<", response.text)[0]
        try:
            self.assertEqual(">注销<", result)
        except Exception as e:
            print(e)

#
# if __name__ == '__main__':
#     Login().test_case01()
