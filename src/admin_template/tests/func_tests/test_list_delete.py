import unittest
import time

from selenium.webdriver.common.by import By
from .base import FunctionalTest


class DraftListDeleteTestCase(FunctionalTest):

    @unittest.skip("跳过删除")
    def test_list_delete(self):
        # 已是登录用户
        self.to_page_list()
        # 找到删除按钮
        btn = self.browser.find_element(by=By.CLASS_NAME, value='del')
        self.assertIn('删 除', btn.text)
        btn.click()
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
