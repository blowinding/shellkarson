from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    """ 中间件 """

    def process_request(self, request):

        # 0.排除不需要登良就能访问的页面
        if request.path_info in ['/shell/login/', '/image/code/', '/stu/register/',
                                 '/soldier/register/', '/org/register/']:
            return

        # 1.读取当前访问的用户的session信息，读到说明登陆过，就可以继续向后走
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 2.如果没有返回请登录
        return redirect('/shell/login/')

        # 如果方法中没有返回值（返回None），继续向后走
        # 有返回值 HttpResponse，render，redirect，则不再继续向后执行
