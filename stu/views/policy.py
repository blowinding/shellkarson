from stu import models
from stu.utils.uploads import getNewName
from stu.utils.bootstrap import BootStrapModelForm

from django import forms
from django.conf import settings
from django.http import JsonResponse


class PolicyModelForm(BootStrapModelForm):
    class Meta:
        model = models.Policy
        fields = '__all__'


def policy_send(request):
    """ 政策存入 """
    form = PolicyModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        cover_tu = form.cleaned_data.get('cover')
        pic_tu = form.cleaned_data.get('pic')

        form.instance.cover = cover_tu
        form.instance.pic = pic_tu
        form.save()

    return JsonResponse({'code': 200, 'msg': '创建成功'})


def policy_list(request):
    queryset = models.Policy.objects.all().order_by('-id')

    plc_list = []
    for obj in queryset:
        dic = {}
        dic['bulk'] = obj.bulk
        dic['policyType'] = obj.policyType
        dic['timeStamp'] = obj.timeStamp
        dic['source'] = obj.source
        dic['webLink'] = obj.webLink
        dic['cover'] = obj.cover
        dic['theme'] = obj.theme
        dic['pic'] = obj.pic
        plc_list.append(dic)

    return JsonResponse(plc_list, safe=False)
