import requests

from django.contrib.auth.models import User
from bs4 import BeautifulSoup


class LoginPass:
    def __init__(self, url: str):
        self.username = "admin"
        self.password = "123456"
        self.login_url = url
        self.request = requests.session()

    # 测试数据库 创建用户数据
    def create_user(self):
        User.objects.create_user(
            username=self.username,
            password=self.password
        )

    # csrf
    def get_csrf_input_value(self):
        html = self.request.get(self.login_url)
        soup = BeautifulSoup(html.text, "lxml")
        form_csrf = soup.select(
            'input[name="csrfmiddlewaretoken"]'
        )[0].get('value')

        csrf_cookies = html.cookies["csrftoken"]
        return form_csrf, csrf_cookies

    # 返回登录 session
    def get_login_session(self):
        self.create_user()
        csrf_input, csrf_token = self.get_csrf_input_value()
        # 请求表单
        user_login = {
            "username": self.username,
            "password": self.password,
            "csrfmiddlewaretoken": csrf_input
        }
        # 请求头
        headers = {
            'Cookie': 'csrftoken=' + csrf_token
        }
        # 发送请求
        res = requests.post(
            self.login_url,
            headers=headers,
            data=user_login
        )
        home_cookie = res.request.headers["Cookie"]
        sessionid = home_cookie[home_cookie.index("sessionid=") + 10:]
        return sessionid
