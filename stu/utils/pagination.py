""" 自定义分页组件 """
from django.utils.safestring import mark_safe

'''
使用方法如下，在视图函数中
def pretty_list(request):

    1. 筛选想要的数据
    queryset = models.PrettyNum.objects.all()

    2. 实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
        'queryset': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html()  # 生成页码
    }

    return render(request, 'pretty_list.html', context)
    
HTML文件中
<nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
        {{ page_string }}
        <div style="width: 100px;">
            <form class="d-flex" method="get">
                <input class="form-control me-2" type="text" name="page" placeholder="to" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">
                    To
                </button>
            </form>
        </div>
    </ul>
</nav>
'''


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_params='page', plus=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据给他进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_params: 在url中传递的获取分页的参数: /pretty/list/?page=1
        :param plus: 显示当前页的前后几页
        """

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_params = page_params

        page = request.GET.get(page_params, '1')  # 获取当前页
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        # 数据总条数
        total_count = queryset.count()

        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 数据库的数据比较少，没达到11页
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count + 1
        else:
            # 数据库数据够多

            # 当前页<5
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页>5
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count + 1
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_params, [1])

        # 首页
        page_str_list.append('<li class="page-item"><a class="page-link" href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_params, [self.page - 1])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_params, [1])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 中间页
        for i in range(start_page, end_page):
            self.query_dict.setlist(self.page_params, [i])
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_params, [self.page + 1])
            after = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_params, [self.total_page_count])
            after = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(after)

        # 尾页
        self.query_dict.setlist(self.page_params, [self.total_page_count])
        page_str_list.append(
            '<li class="page-item"><a class="page-link" href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        page_string = mark_safe(''.join(page_str_list))
        return page_string
