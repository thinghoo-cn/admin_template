import unittest
import time

from selenium.webdriver.common.by import By
from .base import FunctionalTest


@unittest.skip(reason="invalid test")
class DraftListTestCase(FunctionalTest):
    def test_list(self):
        # 已是登录用户
        self.to_page_list()
        # title
        self.assertIn("发版草稿列表", self.browser.title)
        # panel
        panel = self.browser.find_element(by=By.CLASS_NAME, value="panel-heading")
        self.assertIn("发版草稿列表", panel.text)
