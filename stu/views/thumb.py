from stu import models

from django.http import JsonResponse


def thumb(request):
    # 表单形式获取前端数据
    post_id = request.POST.get('id')
    num = request.POST.get('thumb')
    models.Post.objects.filter(id=post_id).update(thumb=num)

    return JsonResponse({'code': 200, 'msg': 'good'})
