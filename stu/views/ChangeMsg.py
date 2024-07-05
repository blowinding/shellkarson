import os

from django import forms
from django.conf import settings
from django.http import JsonResponse

from stu import models
from stu.utils.encrypt import md5
from stu.utils.uploads import getNewName


class StuMsgEditModelForm(forms.ModelForm):
    class Meta:
        model = models.StuInfo
        exclude = ['sch_No', 'name', 'type', 'profile', 'phoneNo']


def StuMsg_edit(request):
    sch_No = request.GET.get('schNo')
    obj = models.StuInfo.objects.filter(sch_No=sch_No).first()
    pwd_origin = obj.password
    stu_form = StuMsgEditModelForm(data=request.POST, instance=obj)

    if stu_form.is_valid():
        print(1)
    else:
        print(0)

    if stu_form.is_valid():
        print(stu_form.cleaned_data)
        pwd_change = stu_form.cleaned_data.get('password')
        if pwd_change == pwd_origin:
            stu_form.save()
        else:
            stus_form = stu_form.save(commit=False)
            pwd_new = md5(pwd_change)
            stus_form.password = pwd_new
            stus_form.save()

    return JsonResponse({'code': 200, 'msg': '更改成功'})


class SoldierMsgEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Soldier
        exclude = ['sch_No', 'type', 'name', 'profile', 'phoneNo']


def SoldierMsg_edit(request):
    sch_No = request.GET.get('schNo')
    obj = models.Soldier.objects.filter(sch_No=sch_No).first()
    pwd_origin = obj.password
    soldier_form = SoldierMsgEditModelForm(data=request.POST, instance=obj)

    if soldier_form.is_valid():
        print(1)
    else:
        print(0)

    if soldier_form.is_valid():
        pwd_change = soldier_form.cleaned_data.get('password')
        if pwd_change == pwd_origin:
            soldier_form.save()
        else:
            sold_form = soldier_form.save(commit=False)
            pwd_new = md5(pwd_change)
            sold_form.password = pwd_new
            sold_form.save()

    return JsonResponse({'code': 200, 'msg': '更改成功'})


class OrgMsgEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Org
        exclude = ['sch_No', 'profile']


def OrgMsg_edit(request):
    sch_No = request.GET.get('schNo')
    obj = models.Org.objects.filter(sch_No=sch_No).first()
    pwd_origin = obj.password
    org_form = OrgMsgEditModelForm(data=request.POST, instance=obj)
    if org_form.is_valid():

        print(1)
    else:
        print(0)

    if org_form.is_valid():
        pwd_change = org_form.cleaned_data.get('password')
        if pwd_change == pwd_origin:
            org_form.save()
        else:
            orgn_form = org_form.save(commit=False)
            pwd_new = md5(pwd_change)
            orgn_form.password = pwd_new
            orgn_form.save()

    return JsonResponse({'code': 200, 'msg': '更改成功'})
