"""
自定义的分页组件
# 分页组件说明
# 在视图函数中
def pretty_list(request):
    # 1、 根据自己的情况去筛选所需要的数据
    queryset = models.PrettyNum.objects.filter(
    **data_dict).order_by("-level")
    # 2、 实例化分页对象
    page_object = Pagenation(request, queryset)
    # 3、
    context = {
        # 分完页的数据
        "queryset": page_object.page_queryset,
        # 生成 分页 Html 代码
        "page_string": page_object.html(),
    }
    return render(request, "pretty_list.html", context)

# 在 html 页面中
    {# 数据展示 #}
    {% for obj in queryset %}
        {{ obj.xx }}
    {% endfor %}

    {#  分页框     #}
    <ul class="pagination">
        {{ page_string }}
    </ul>
"""

from django.utils.safestring import mark_safe
import copy
from django.http.request import QueryDict


class Pagenation(object):

    def __init__(self, request, queryset,
                 page_param="page", page_size=10, plus=5):
        """
         :param request: 请求对象
         :param queryset: 数据库查询的符合条件的数据（根据这个数据进行分页处理）
         :param page_param: 在 url 中 获取分页的参数（第几页） 例如：/pretty/list/?page=1
         :param page_size: 每页显示多少条数据
         :param plus: 分页栏 显示当前页的前或后几页 （页码）
         """
        # 获取当前 GET 请求传递来的参数 转字符串 目的拼接请求
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, 1)
        page = int(page)
        # 分页
        self.page = page  # 页数
        self.page_size = page_size  # 每页数据量
        self.start = (page - 1) * page_size  # 起始页
        self.end = page * page_size  # 结束页
        self.page_queryset = queryset[self.start:self.end]  # 已分完页的数据
        self.plus = plus  # 加载的页面数

        # 获取数据库数据总条数
        total_count = queryset.count()

        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        # 总页码数量
        self.total_page_count = total_page_count

    def html(self):
        # 计算出前五 后五页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据两比较少
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据量较多
            # 负数边界( 小的极值 ）
            if self.page <= self.page:
                start_page = 1
                end_page = 2 * self.page + 1
            else:
                # 当前页 > 5
                # 当前页 + 5 > 总页面
                if self.page + self.plus > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        # 生成 页码HTML
        page_str_list = []
        # 首页
        # GET 请求参数拼接
        # 前一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<a class="pagination-previous" href="?{}">Previous</a>'\
                .format(self.query_dict.urlencode())
        else:
            prev = '<a class="pagination-previous disabled" ' \
                   'href="?{}">Previous</a>'
        page_str_list.append(prev)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            back = '<a class="pagination-next" ' \
                   'href="?{}">Next page</a>'\
                .format(self.query_dict.urlencode())
        else:
            back = '<a class="pagination-next" href="#">Next page</a>'
        page_str_list.append(back)

        page_str_list.append('<ul class="pagination-list">')
        # 页数
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li><a class="pagination-link is-current" ' \
                      'href="?{}">{}</a></li'\
                    .format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a class="pagination-link"  ' \
                      'href="?{}">{}</a></li>'\
                    .format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)
        page_str_list.append('</ul>')

        # str 转 Html 安全化
        page_string = mark_safe("".join(page_str_list))
        return page_string
