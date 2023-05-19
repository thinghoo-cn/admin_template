# Admin template

这是 CDServer 生成的模板。

希望可以：

1. 定制化 sidebar，自动生成；
2. 继承模板，多开发一些有价值的功能组件。


## 安装与配置

- 安装: `pip install admin_template` or `poetry add admin_template`
- 配置：

settings.py:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
+    "bootstrap3",
+    "admin_template",
+    "thinghoo_adminlte2",
+    "django_adminlte",
]
```

## 使用

- `views`: `from admin_template.views.generic import SidebarTemplateView`: views: 使用 SideBar 时，可以继承 `SideBarView`:
- `mixins`: `from admin_template.views.mixin import SidebarMixin`: 集成 mixin 的时候，可以通过设置`sidebar`来完成系统部署。

例如：

```py
from admin_template.views.generic import SidebarTemplateView


class HomeView(SidebarTemplateView):
    template_name = "admin_template/home.html"
```

### sidebar 数据结构

```python
default_sidebar = {
    "system_title": "ADMIN TEMPLATE",
    "bars": [
        {
            "entity": "product",
            "name": "产品列表",
            "logo": "fa-product-hunt",
        },
        {
            "entity": "project",
            "name": "项目列表",
            "logo": "fa-product-hunt",
        },
        {
            "entity": "version",
            "name": "版本",
            "logo": "fa-play-circle",
            "sub_menu": [
                {
                    "entity": "draft",
                    "name": "草稿",
                },
            ],
        },
    ],
}
```