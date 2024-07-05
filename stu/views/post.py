from stu import models
from stu.utils.uploads import getNewName
from stu.utils.bootstrap import BootStrapModelForm

from django import forms
from django.conf import settings
from django.http import JsonResponse


class PostModelForm(BootStrapModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'


def post_add(request):
    """ 帖子存入 """
    form = PostModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        pic_tu = form.cleaned_data.get('pic')
        form.instance.pic = pic_tu

        form.save()
    post_id = models.Post.objects.all().order_by('-id').first().id
    return JsonResponse({'code': 200, 'msg': '创建成功', 'id': post_id})


def post_list(request):
    queryset = models.Post.objects.all().order_by('-id')

    pos_list = []
    for obj in queryset:
        replyset = models.Reply.objects.filter(post=obj.id).order_by('-id')
        com = []
        dic = {}
        dic['id'] = obj.id
        dic['theme'] = obj.theme
        dic['bulk'] = obj.bulk
        dic['pic'] = obj.pic
        dic['timeStamp'] = obj.timeStamp
        dic['schNo'] = obj.schNo
        for i in replyset:
            dict = {}
            dict['schNo'] = i.schNo
            dict['bulk'] = i.bulk
            dict['pic'] = i.pic
            dict['timeStamp'] = i.timeStamp
            com.append(dict)
        dic['reply'] = com
        dic['thumb'] = obj.thumb
        pos_list.append(dic)

    return JsonResponse(pos_list, safe=False)


def post_delete(request):
    nid = request.POST.get('id')
    models.Post.objects.filter(id=nid).delete()
    return JsonResponse({'code': 200, 'msg': '删除成功'})
