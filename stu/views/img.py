from stu.utils.uploads import getNewName
from stu import models
from django.conf import settings
from django.http import JsonResponse, HttpResponse

import time
import random
from datetime import datetime


def add_stu_image(request):
    # 获取一个文件管理器对象
    file = request.FILES['profile']

    # 保存文件
    new_name = getNewName('stu')  # 具体实现在自己写的uploads.py下
    # 将要保存的地址和文件名称
    path_ = f'{settings.MEDIA_ROOT}/norstu/{new_name}'
    path = path_.replace('\\', '/')
    print(path)
    # 分块保存image
    content = file.chunks()
    with open(path, 'wb') as f:
        for i in content:
            f.write(i)

    # 上传文件名称到数据库
    models.StuInfo.objects.filter(sch_No='2227777777').update(profile=path)
    # 返回的httpresponse
    return HttpResponse('ok')


def upload(request):
    rec_file = request.FILES.get('file')

    time_for = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(100, 999))
    file_Name = f'{time_for}-{rec_file.name}'

    with open(f'images/{file_Name}', 'wb') as f:
        f.write(rec_file.read())

    return HttpResponse({"http://8.130.46.21:8000/images/" + file_Name})
