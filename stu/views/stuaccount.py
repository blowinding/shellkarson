from django import forms
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from stu import models
from stu.utils.encrypt import md5
from stu.utils.uploads import getNewName
from stu.utils.bootstrap import BootstrapForm, BootStrapModelForm

import re
import json
import random
from datetime import datetime


class StuModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 确保输入的密码不可视,同时错误不删除
    )

    class Meta:
        model = models.StuInfo
        fields = ['name', 'profile', 'nick', 'sch_No', 'gender', 'insit', 'selfIntro',
                  'phoneNo', 'qqNo', 'wechatNo', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')  # 已经加完密
        confirm = md5(self.cleaned_data.get('confirm_password'))  # 确认的密码加密
        if confirm != pwd:
            return JsonResponse({'error': '两次密码不一致'})
        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


def stu_register(request):
    """ 注册学生 """
    form = StuModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        sch_No = form.cleaned_data.get('sch_No')
        if len(sch_No) != 10:
            return JsonResponse({'code': 500, 'error': '学号格式不正确'})

        stu_obj = models.StuInfo.objects.filter(sch_No=sch_No).exists()
        if stu_obj:
            return JsonResponse({'code': 500, 'error': '对应该学号用户已经注册'})
        soldier_obj = models.Soldier.objects.filter(sch_No=sch_No).exists()
        if soldier_obj:
            return JsonResponse({'code': 500, 'error': '对应该学号用户已经注册'})

        pwd = form.cleaned_data.get('password')
        pwd_con = form.cleaned_data.get('confirm_password')
        if pwd != pwd_con:
            return JsonResponse({'code': 500, 'error': '两次输入的密码不一致'})

        # 检测手机号是否已经注册过
        n = form.cleaned_data.get('phoneNo')
        if len(n) != 11:
            return JsonResponse({'code': 500, 'error': '手机号格式错误'})
        if not re.match(r'13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89]\d{8}$', n):
            return JsonResponse({'code': 500, 'error': '手机号格式错误'})

        stu_obj1 = models.StuInfo.objects.filter(phoneNo=n).exists()
        if stu_obj1:
            return JsonResponse({'code': 500, 'error': '该手机号已经被注册'})
        solder_obj1 = models.Soldier.objects.filter(phoneNo=n).exists()
        if solder_obj1:
            return JsonResponse({'code': 500, 'error': '该手机号已经被注册'})

        profile_tu = form.cleaned_data.get('profile')
        form.instance.profile = profile_tu

        form.save()

    return JsonResponse({'code': 200})


class SoldierModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 确保输入的密码不可视,同时错误不删除
    )

    class Meta:
        model = models.Soldier
        fields = ['name', 'nick', 'profile', 'sch_No', 'gender', 'insit', 'selfIntro',
                  'phoneNo', 'qqNo', 'wechatNo', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')  # 已经加完密
        confirm = md5(self.cleaned_data.get('confirm_password'))  # 确认的密码加密
        if confirm != pwd:
            return JsonResponse({'error': '两次密码不一致'})
        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


def soldier_register(request):
    """ 注册大学生士官 """
    form = SoldierModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        # 检测学号是否已经存在
        sch_No = form.cleaned_data.get('sch_No')
        if len(sch_No) != 10:
            return JsonResponse({'code': 500, 'error': '学号格式不正确'})

        soldier_obj = models.Soldier.objects.filter(sch_No=sch_No).exists()
        if soldier_obj:
            return JsonResponse({'code': 500, 'error': '对应该学号用户已经注册'})
        stu_obj = models.StuInfo.objects.filter(sch_No=sch_No).exists()
        if stu_obj:
            return JsonResponse({'code': 500, 'error': '对应该学号用户已经注册'})

        pwd = form.cleaned_data.get('password')
        pwd_con = form.cleaned_data.get('confirm_password')
        if pwd != pwd_con:
            return JsonResponse({'code': 500, 'error': '两次输入的密码不一致'})

        # 检测手机号是否已经注册过
        n = form.cleaned_data.get('phoneNo')
        if len(n) != 11:
            return JsonResponse({'code': 500, 'error': '手机号格式错误'})
        if not re.match(r'13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89]\d{8}$', n):
            return JsonResponse({'code': 500, 'error': '手机号格式错误'})

        solder_obj1 = models.Soldier.objects.filter(phoneNo=n).exists()
        if solder_obj1:
            return JsonResponse({'code': 500, 'error': '该手机号已经被注册'})
        stu_obj1 = models.StuInfo.objects.filter(phoneNo=n).exists()
        if stu_obj1:
            return JsonResponse({'code': 500, 'error': '该手机号已经被注册'})

        profile_tu = form.cleaned_data.get('profile')
        form.instance.profile = profile_tu

        form.save()

    return JsonResponse({'code': 200})


class OrgModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 确保输入的密码不可视,同时错误不删除
    )

    class Meta:
        model = models.Org
        fields = ['orgType', 'orgName', 'profile',
                  'orgIntro', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }


def org_register(request):
    """ 社团 """
    global pwd_origin
    form = OrgModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():

        form.instance.sch_No = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))

        pwd_origin = form.cleaned_data.get('password')
        pwd_con = form.cleaned_data.get('confirm_password')
        if pwd_origin != pwd_con:
            return JsonResponse({'code': 500, 'error': '两次输入的密码不一致'})

        profile_tu = form.cleaned_data.get('profile')
        form.instance.profile = profile_tu

        form.instance.password = md5(pwd_origin)

        form.save()

    org_new = models.Org.objects.all().order_by('-id').first()
    sch_No = org_new.sch_No

    return JsonResponse({'code': 200, 'schNo': sch_No, 'pwd': pwd_origin})
