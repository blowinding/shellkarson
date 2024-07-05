import random
from stu import models
from django import forms
from datetime import datetime

from stu.utils.bootstrap import BootStrapModelForm

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


class VolunteerModelForm(BootStrapModelForm):
    class Meta:
        model = models.Volunteer
        fields = '__all__'


def volunteer_add(request):
    """ 志愿者存入 """
    form = VolunteerModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        form.save()

    return JsonResponse({'code': 200, 'msg': '创建成功'})


def volunteer_list(request):
    queryset = models.Volunteer.objects.all().order_by('-id')

    vol_list = []
    for obj in queryset:
        dic = {}
        dic['name'] = obj.name
        dic['insit'] = obj.insit
        dic['contact'] = obj.contact
        dic['subject'] = obj.subject
        dic['major'] = obj.major
        vol_list.append(dic)

    return JsonResponse(vol_list, safe=False)
