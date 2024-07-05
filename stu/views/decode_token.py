import jwt
from jwt import exceptions

from stu import models
from stu.utils.jwt_auth import create_token

from django.conf import settings
from django.http import JsonResponse, HttpResponse

from rest_framework.exceptions import AuthenticationFailed


def decode_token(request):
    token = request.GET.get('token')
    salt = settings.SECRET_KEY

    try:
        payload = jwt.decode(token, salt, True)['schNo']
        stu_object = models.StuInfo.objects.filter(sch_No=payload).first()
        soldier_object = models.Soldier.objects.filter(sch_No=payload).first()
        org_object = models.Org.objects.filter(sch_No=payload).first()
        if stu_object:
            token_new = create_token({'schNo': stu_object.sch_No})
            res_dict = {
                'code': 200,
                'pass': 'true',
                'type': stu_object.type,
                'name': stu_object.name,
                'nick': stu_object.nick,
                'profile': stu_object.profile,
                'schNo': stu_object.sch_No,
                'gender': stu_object.gender,
                'insit': stu_object.insit,
                'selfIntro': stu_object.selfIntro,
                'phoneNo': stu_object.phoneNo,
                'qqNo': stu_object.qqNo,
                'wechatNo': stu_object.wechatNo,
                'pwd': stu_object.password,
                'token': token_new
            }
            return JsonResponse(res_dict)

        if soldier_object:
            token_new = create_token({'schNo': soldier_object.sch_No})
            res_dict = {
                'code': 1001,
                'pass': 'true',
                'type': soldier_object.type,
                'name': soldier_object.name,
                'nick': soldier_object.nick,
                'profile': soldier_object.profile,
                'schNo': soldier_object.sch_No,
                'gender': soldier_object.gender,
                'insit': soldier_object.insit,
                'selfIntro': soldier_object.selfIntro,
                'phoneNo': soldier_object.phoneNo,
                'qqNo': soldier_object.qqNo,
                'wechatNo': soldier_object.wechatNo,
                'pwd': soldier_object.password,
                'token': token_new,
            }
            return JsonResponse(res_dict)

        if org_object:
            token_new = create_token({'schNo': org_object.sch_No})
            res_dict = {
                'code': 1001,
                'token': token_new,
                'pass': 'true',
                'orgType': org_object.orgType,
                'orgName': org_object.orgName,
                'profile': org_object.profile,
                'schNo': org_object.sch_No,
                'orgIntro': org_object.orgIntro,
                'pwd': org_object.password,
                'type': '组织',
            }
            return JsonResponse(res_dict)
    except exceptions.ExpiredSignatureError:
        return JsonResponse({'code': 1003, 'error': 'token已失效', 'pass': 'false'})
    except jwt.DecodeError:
        return JsonResponse({'code': 1003, 'error': 'token认证失败', 'pass': 'false'})
    except jwt.InvalidTokenError:
        return JsonResponse({'code': 1003, 'error': '非法的token', 'pass': 'false'})

    return HttpResponse('bj')
