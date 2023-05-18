import unittest
import time

from selenium.webdriver.common.by import By
from .base import FunctionalTest


@unittest.skip(reason="invalid test")
class DraftListAddTestCase(FunctionalTest):
    def test_list_add(self):
        # 已是登录用户
        self.to_page_list()

        # 找到新建按钮键
        add_btn = self.browser.find_element(by=By.CLASS_NAME, value="add-draft")
        self.assertIn("新建发版草稿", add_btn.text)
        add_btn.click()
        time.sleep(1)

        # ----------------- 获取表单 ---------------
        # 产品名称
        input_product_name = self.browser.find_element(by=By.NAME, value="product_name")
        self.assertEqual(input_product_name.get_attribute("placeholder"), "产品名称(必填)")
        # 发行版本号
        input_release_version = self.browser.find_element(by=By.NAME, value="release_version")
        self.assertEqual(input_release_version.get_attribute("placeholder"), "发行版本号（必填）")
        # 发行版本号
        input_hash_front = self.browser.find_element(by=By.NAME, value="hash_front")
        self.assertEqual(input_hash_front.get_attribute("placeholder"), "前端 Commit hash（必填）")
        # 发行版本号
        input_hash_back = self.browser.find_element(by=By.NAME, value="hash_back")
        self.assertEqual(input_hash_back.get_attribute("placeholder"), "后端 Commit Hash (必填)")
        # 生成草稿按钮
        draft_btn = self.browser.find_element(by=By.CLASS_NAME, value="draft-btn")
        self.assertIn("生成发版草稿", draft_btn.text)

        # ----------------- 填写表单 ---------------
        input_product_name.send_keys("QMS")
        input_release_version.send_keys("v9.1")
        input_hash_front.send_keys("213124213412312")
        input_hash_back.send_keys("2312412312132412")
        time.sleep(1)
        draft_btn.click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
