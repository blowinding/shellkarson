from stu import models

from django.http import JsonResponse


def stu_info(request):
    stu_obj = models.StuInfo.objects.all()
    stu_list = []
    for obj in stu_obj:
        ret_obj = {
            'sch_No': obj.sch_No,
            'nick': obj.nick,
            'profile': obj.profile
        }
        stu_list.append(ret_obj)

    return JsonResponse(stu_list, safe=False)


def soldier_info(request):
    soldier_obj = models.Soldier.objects.all()
    soldier_list = []
    for obj in soldier_obj:
        ret_obj = {
            'sch_No': obj.sch_No,
            'nick': obj.nick,
            'profile': obj.profile
        }
        soldier_list.append(ret_obj)

    return JsonResponse(soldier_list, safe=False)


def org_info(request):
    org_obj = models.Org.objects.all()
    org_list = []
    for obj in org_obj:
        ret_obj = {
            'sch_No': obj.sch_No,
            'nick': obj.orgName,
            'profile': obj.profile
        }
        org_list.append(ret_obj)

    return JsonResponse(org_list, safe=False)


def profile_to_info(request):
    """ 根据头像获得用户信息 """
    schNo = request.GET.get('schNo')
    stu_object = models.StuInfo.objects.filter(sch_No=schNo).first()
    soldier_object = models.Soldier.objects.filter(sch_No=schNo).first()
    org_object = models.Org.objects.filter(sch_No=schNo).first()

    if stu_object:
        res_dict = {
            'code': 200,
            'nick': stu_object.nick,
            'profile': stu_object.profile,
            'schNo': schNo,
            'gender': stu_object.gender,
            'insit': stu_object.insit,
            'selfIntro': stu_object.selfIntro,
            'phoneNo': stu_object.phoneNo,
            'qqNo': stu_object.qqNo,
            'wechatNo': stu_object.wechatNo,
        }
        return JsonResponse(res_dict)

    if soldier_object:
        res_dict = {
            'code': 200,
            'nick': soldier_object.nick,
            'profile': soldier_object.profile,
            'schNo': schNo,
            'gender': soldier_object.gender,
            'insit': soldier_object.insit,
            'selfIntro': soldier_object.selfIntro,
            'phoneNo': soldier_object.phoneNo,
            'qqNo': soldier_object.qqNo,
            'wechatNo': soldier_object.wechatNo,
        }
        return JsonResponse(res_dict)

    if org_object:
        res_dict = {
            'code': 200,
            'orgType': org_object.orgType,
            'orgName': org_object.orgName,
            'profile': org_object.profile,
            'schNo': schNo,
            'orgIntro': org_object.orgIntro,
        }
        return JsonResponse(res_dict)

    if not stu_object:
        if not soldier_object:
            if not org_object:
                return JsonResponse({'code': 500, 'error': '没有该学生'})
