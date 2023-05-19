"""
Sidebar type.


{% include 'adminlte/lib/_sidebar_module.html' with entity='team' name='团队管理' logo='fa-user' %}
{% include 'adminlte/lib/_sidebar_module.html' with entity='product' name='产品列表' logo='fa-product-hunt' %}
{% include 'adminlte/lib/_sidebar_module.html' with entity='project' name='项目列表' logo='fa-product-hunt' %}
{% include 'adminlte/lib/_sidebar_module.html' with entity='sprint' name='迭代追踪' logo='fa-fire' %}
{% include 'adminlte/lib/_sidebar_module.html' with entity='issue' name='交付工单' logo='fa-fire' %}

<li class='treeview {% is_active "/version/" %}'>
    <a href="#"><i class="fa fa-play-circle"></i> <span>版本</span> <i class="fa fa-angle-left pull-right"></i></a>
    <ul class="treeview-menu">
        <li> <a href="/version/draft/list">发版草稿</a></li>
    </ul>
    <ul class="treeview-menu">
        <li> <a href="/version/review/list">发版审核</a></li>
    </ul>
    <ul class="treeview-menu">
        <li> <a href="/version/release/list">发版日志</a></li>
    </ul>
</li>
"""

# Example sidebar.
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
