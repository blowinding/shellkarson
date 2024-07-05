import jwt
import datetime
from stu import models
from stu.utils.encrypt import md5
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from jwt import exceptions

from stu.utils.jwt_auth import create_token
from stu.extensions.auth import JwtQueryParamsAuthentication


class ProLoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        schNo = request.data.get('sch_No')
        pwd_ = request.data.get('password')
        pwd = md5(pwd_)

        # 判断登录对象
        stu_object = models.StuInfo.objects.filter(sch_No=schNo, password=pwd).first()
        soldier_object = models.Soldier.objects.filter(sch_No=schNo, password=pwd).first()
        org_object = models.Org.objects.filter(sch_No=schNo, password=pwd).first()
        if not stu_object:
            if not soldier_object:
                if not org_object:
                    return Response({'code': 1000, 'error': '用户名或密码错误', 'pass': 'false'})

        if stu_object:
            token = create_token({'schNo': stu_object.sch_No})
            res_dict = {
                'code': 1001,
                'pass': 'true',
                'type': stu_object.type,
                'name': stu_object.name,
                'nick': stu_object.nick,
                # stu_object.profile 获取的是图片文件
                'profile': stu_object.profile,  # 仅展示图片路径
                'schNo': schNo,
                'gender': stu_object.gender,
                'insit': stu_object.insit,
                'selfIntro': stu_object.selfIntro,
                'phoneNo': stu_object.phoneNo,
                'qqNo': stu_object.qqNo,
                'wechatNo': stu_object.wechatNo,
                'pwd': stu_object.password,
                'token': token,
            }
            return Response(res_dict)

        if soldier_object:
            token = create_token({'schNo': soldier_object.sch_No})
            res_dict = {
                'code': 1001,
                'pass': 'true',
                'type': soldier_object.type,
                'name': soldier_object.name,
                'nick': soldier_object.nick,
                'profile': soldier_object.profile,
                'schNo': schNo,
                'gender': soldier_object.gender,
                'insit': soldier_object.insit,
                'selfIntro': soldier_object.selfIntro,
                'phoneNo': soldier_object.phoneNo,
                'qqNo': soldier_object.qqNo,
                'wechatNo': soldier_object.wechatNo,
                'pwd': soldier_object.password,
                'token': token,
            }
            return Response(res_dict)

        if org_object:
            token = create_token({'schNo': org_object.sch_No})
            res_dict = {
                'code': 1001,
                'token': token,
                'pass': 'true',
                'orgType': org_object.orgType,
                'orgName': org_object.orgName,
                'profile': org_object.profile,
                'schNo': schNo,
                'orgIntro': org_object.orgIntro,
                'pwd': org_object.password,
                'type': '组织',
            }
            return Response(res_dict)


class ProInfoView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response('info')
