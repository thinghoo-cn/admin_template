import unittest
import time

from selenium.webdriver.common.by import By
from .base import FunctionalTest


class DraftListUpdateTestCase(FunctionalTest):

    @unittest.skip("跳过更新")
    def test_list_view(self):
        # 已是登录用户
        self.to_page_list()
        # 查看按钮
        btn = self.browser.find_element(by=By.CLASS_NAME, value='edit')
        self.assertIn('编 辑', btn.text)
        btn.click()
        time.sleep(1)

        # 返回按钮
        back_btn = self.browser.find_element(
            by=By.CLASS_NAME, value='back-list')
        self.assertIn('返回', back_btn.text)
        btn.click()
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
