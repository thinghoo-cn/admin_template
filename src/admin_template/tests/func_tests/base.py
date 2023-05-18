import os

from selenium import webdriver
from django.conf import settings


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from admin_template.tests.tools.get_csrf_info import LoginPass


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.staging_server = os.environ.get("STAGING_SERVER")
        if self.staging_server:
            self.live_server_url = "http://" + self.staging_server

    def tearDown(self) -> None:
        self.browser.quit()

    # 创建 Session 对话 跳过登录
    def take_cookies(self):
        login_pass = LoginPass(self.live_server_url + "/user/login/")
        sessionid = login_pass.get_login_session()
        self.browser.get(self.live_server_url + "/404/")
        # 添加 cookie 访问
        self.browser.add_cookie(
            dict(
                name=settings.SESSION_COOKIE_NAME,
                value=sessionid,
                path="/",
            )
        )

    # to Page List
    def to_page_list(self):
        # 已是登录用户
        self.take_cookies()
        # 访问首页
        self.browser.get(self.live_server_url)
        # 找到跳转按钮
        btn = self.browser.find_element(by=By.CLASS_NAME, value="draft-list")
        btn.click()
