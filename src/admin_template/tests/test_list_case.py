import unittest
from django.test import TestCase
from django.http import HttpRequest

from ..views.home import home_page
from admin_template.tests.tools.get_csrf_info import LoginPass


@unittest.skip(reason="invalid test")
class ListTestCase(TestCase):
    # 测试 URL 解析的 template
    def test_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "admin_template/base.html")

    # 测试　访问界面 基本内容　（GET）
    def test_home_html_get(self):
        # 向 登录函数 发送请求 获得响应信息
        request = HttpRequest()
        request.method = "GET"
        request.session = {}
        response = home_page(request)
        # utf8 解码 为html文本
        html = response.content.decode("utf8")
        html = html.replace("\n", "")
        # 断言文本是否符合预期
        self.assertIn("<title>CD Server</title>", html)
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertTrue(html.endswith("</html>"))
