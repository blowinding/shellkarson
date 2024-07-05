from stu import models

from django.http import JsonResponse


def search_list(request):
    dic = {}  # 整体搜索到的值返回的字典

    # 搜索政策
    data_dict_policy = {}
    search_data_policy = request.GET.get('s')

    if search_data_policy:
        data_dict_policy['theme__contains'] = search_data_policy
        qset_policy = models.Policy.objects.filter(**data_dict_policy).order_by('-id')

        policy_list = []
        for obj in qset_policy:
            dict_policy = {}
            dict_policy['bulk'] = obj.bulk
            dict_policy['policyType'] = obj.policyType
            dict_policy['timeStamp'] = obj.timeStamp
            dict_policy['source'] = obj.source
            dict_policy['webLink'] = obj.webLink
            dict_policy['cover'] = obj.cover
            dict_policy['theme'] = obj.theme
            dict_policy['pic'] = obj.pic
            policy_list.append(dict_policy)

        dic['policy'] = policy_list

    # 搜索活动
    data_dict_act = {}
    search_data_act = request.GET.get('s')
    if search_data_act:
        data_dict_act['theme__contains'] = search_data_act
        qset_act = models.Act.objects.filter(**data_dict_act).order_by('-id')
        act_list = []
        for obj in qset_act:
            dict_act = {}
            dict_act['bulk'] = obj.bulk
            dict_act['type'] = obj.type
            dict_act['timeStamp'] = obj.timeStamp
            dict_act['theme'] = obj.theme
            dict_act['pic'] = obj.pic
            dict_act['cover'] = obj.cover
            act_list.append(dict_act)

        dic['act'] = act_list

    # 搜索帖子
    data_dict_post = {}
    search_data_post = request.GET.get('s')
    if search_data_post:
        data_dict_post['theme__contains'] = search_data_post
        qset_post = models.Post.objects.filter(**data_dict_post).order_by('-id')
        post_list = []
        for obj in qset_post:
            dict_post = {}
            replyset = models.Reply.objects.filter(post=obj.id).order_by('-id')
            com = []

            dict_post['theme'] = obj.theme
            dict_post['bulk'] = obj.bulk
            dict_post['pic'] = obj.pic
            dict_post['timeStamp'] = obj.timeStamp
            dict_post['schNo'] = obj.schNo
            for i in replyset:
                dict = {}
                dict['schNo'] = i.schNo
                dict['bulk'] = i.bulk
                dict['pic'] = i.pic
                dict['timeStamp'] = i.timeStamp
                com.append(dict)
            dict_post['reply'] = com
            dict_post['thumb'] = obj.thumb
            post_list.append(dict_post)
        dic['post'] = post_list

    # user类
    dic_user = {}

    # 搜索普通学生
    data_dict_stu = {}
    search_data = request.GET.get('s')

    if search_data:
        data_dict_stu['nick__contains'] = search_data
        qset_stu = models.StuInfo.objects.filter(**data_dict_stu).order_by('id')

        stu_list = []
        for obj in qset_stu:
            dict_stu = {}
            dict_stu['type'] = obj.type
            dict_stu['name'] = obj.name
            dict_stu['nick'] = obj.nick
            dict_stu['profile'] = obj.profile
            dict_stu['sch_No'] = obj.sch_No
            dict_stu['gender'] = obj.gender
            dict_stu['insit'] = obj.insit
            dict_stu['selfIntro'] = obj.selfIntro
            dict_stu['phoneNo'] = obj.phoneNo
            dict_stu['qqNo'] = obj.qqNo
            dict_stu['wechatNo'] = obj.wechatNo
            dict_stu['password'] = obj.password
            stu_list.append(dict_stu)

        dic_user['stu'] = stu_list

    # 搜索军人
    data_dict_soldier = {}
    search_data_soldier = request.GET.get('s')

    if search_data_soldier:
        data_dict_soldier['nick__contains'] = search_data_soldier
        qset_soldier = models.Soldier.objects.filter(**data_dict_soldier).order_by('id')

        soldier_list = []
        for obj in qset_soldier:
            dict_soldier = {}
            dict_soldier['type'] = obj.type
            dict_soldier['name'] = obj.name
            dict_soldier['nick'] = obj.nick
            dict_soldier['profile'] = obj.profile
            dict_soldier['sch_No'] = obj.sch_No
            dict_soldier['gender'] = obj.gender
            dict_soldier['insit'] = obj.insit
            dict_soldier['selfIntro'] = obj.selfIntro
            dict_soldier['phoneNo'] = obj.phoneNo
            dict_soldier['qqNo'] = obj.qqNo
            dict_soldier['wechatNo'] = obj.wechatNo
            dict_soldier['password'] = obj.password
            soldier_list.append(dict_soldier)

        dic_user['soldier'] = soldier_list

    # 搜索组织
    data_dict_org = {}
    search_data_org = request.GET.get('s')

    if search_data_org:
        data_dict_org['orgName__contains'] = search_data_org
        qset_org = models.Org.objects.filter(**data_dict_org).order_by('id')

        org_list = []
        for obj in qset_org:
            dict_org = {}
            dict_org['orgType'] = obj.orgType
            dict_org['orgName'] = obj.orgName
            dict_org['profile'] = obj.profile
            dict_org['sch_No'] = obj.sch_No
            dict_org['orgIntro'] = obj.orgIntro
            dict_org['password'] = obj.password
            org_list.append(dict_org)

        dic_user['org'] = org_list

    dic['user'] = dic_user

    return JsonResponse(dic)
