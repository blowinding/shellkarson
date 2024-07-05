from stu import models
from stu.utils.uploads import getNewName
from stu.utils.bootstrap import BootStrapModelForm

from django import forms
from django.conf import settings
from django.http import JsonResponse


class ActModelForm(BootStrapModelForm):
    class Meta:
        model = models.Act
        fields = '__all__'


def act_send(request):
    """ 活动存入 """
    form = ActModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        theme = form.cleaned_data.get('theme')
        if '/' in theme:
            return JsonResponse({'code': 500, 'error': "主题中不能含有'/'"})
        if '\\' in theme:
            return JsonResponse({'code': 500, 'error': "主题中不能含有'\\'"})

        cover_tu = form.cleaned_data.get('cover')
        pic_tu = form.cleaned_data.get('pic')

        form.instance.cover = cover_tu
        form.instance.pic = pic_tu
        form.save()

    return JsonResponse({'code': 200, 'msg': '创建成功'})


def act_list(request):
    queryset = models.Act.objects.all().order_by('-id')

    acts_list = []
    for obj in queryset:
        dic = {}
        dic['bulk'] = obj.bulk
        dic['type'] = obj.type
        dic['timeStamp'] = obj.timeStamp
        dic['theme'] = obj.theme
        dic['pic'] = obj.pic
        dic['cover'] = obj.cover
        acts_list.append(dic)

    return JsonResponse(acts_list, safe=False)
