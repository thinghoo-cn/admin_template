from dataclasses import dataclass


@dataclass
class HeaderItem:
    url: str
    icon: str
    name: str

    # <li class='{% is_active "/" %}'>
    #     <a href="/">
    #         <i class="fa fa-dashboard"></i> <span>主页</span>
    #     </a>
    # </li>


@dataclass
class HeaderGroup:
    url: str

    header_items: list[HeaderItem]
    pass


home = HeaderItem(url="/", icon="fa fa-dashboard", name="主页")

header_list = [
    home,
]


class HeaderList(HeaderItem):
    header_list = header_list

    @staticmethod
    def to_django_context():
        return header_list
