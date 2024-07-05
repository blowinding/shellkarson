from stu import models
from stu.utils.uploads import getNewName
from stu.utils.bootstrap import BootStrapModelForm

from django import forms
from django.conf import settings
from django.http import JsonResponse


class ReplyModelForm(BootStrapModelForm):
    class Meta:
        model = models.Reply
        exclude = ['post']


def reply_add(request):
    """ 评论存入 """
    post_id = request.POST.get('id')
    post = models.Post.objects.filter(id=post_id).first()

    form = ReplyModelForm(data=request.POST)

    if form.is_valid():
        print(1)
    else:
        print(0)

    if form.is_valid():
        pic_tu = form.cleaned_data.get('pic')
        form.instance.pic = pic_tu

        reply_form = form.save(commit=False)
        reply_form.post_id = post.id
        reply_form.save()

    return JsonResponse({'code': 200, 'msg': '创建成功'})
