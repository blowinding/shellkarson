from django.db import models


# Create your models here.

class StuInfo(models.Model):
    """ 学生信息表 """
    objects = None
    name = models.CharField(verbose_name='姓名', max_length=16)
    nick = models.CharField(verbose_name='昵称', max_length=32)
    profile = models.CharField(max_length=256, blank=True, null=True, verbose_name='用户头像')
    sch_No = models.CharField(verbose_name='学号', max_length=10)
    gender = models.CharField(verbose_name='性别', max_length=16)
    insit = models.CharField(verbose_name='书院', max_length=16)
    selfIntro = models.TextField(verbose_name='个人简介', null=True, blank=True, default='在这里介绍自己')
    phoneNo = models.CharField(verbose_name='手机号', max_length=11)  # 选择是否展示
    qqNo = models.CharField(verbose_name='QQ号码', null=True, blank=True, max_length=10)  # 选择是否展示
    wechatNo = models.CharField(verbose_name='微信id', null=True, blank=True, max_length=32)  # 选择是否展示
    password = models.CharField(verbose_name='密码', max_length=32)  # 不予展示
    type = models.CharField(verbose_name='类型', max_length=16, default='学生')


class Soldier(models.Model):
    """ 军人信息表 """
    objects = None
    name = models.CharField(verbose_name='姓名', max_length=16)
    nick = models.CharField(verbose_name='昵称', max_length=32)
    profile = models.CharField(max_length=256, blank=True, null=True, verbose_name='用户头像')
    sch_No = models.CharField(verbose_name='学号', max_length=10)
    gender = models.CharField(verbose_name='性别', max_length=16)
    insit = models.CharField(verbose_name='书院', max_length=16)
    selfIntro = models.TextField(verbose_name='个人简介', null=True, blank=True, default='在这里介绍自己')
    phoneNo = models.CharField(verbose_name='手机号', max_length=11)  # 选择是否展示
    qqNo = models.CharField(verbose_name='QQ号码', null=True, blank=True, max_length=10)  # 选择是否展示
    wechatNo = models.CharField(verbose_name='微信id', null=True, blank=True, max_length=32)  # 选择是否展示
    password = models.CharField(verbose_name='密码', max_length=32)  # 不予展示
    type = models.CharField(verbose_name='类型', max_length=16, default='军人')


class Org(models.Model):
    sch_No = models.CharField(verbose_name='组织编码', max_length=32)
    orgType = models.CharField(verbose_name='组织类型', max_length=16)
    orgName = models.CharField(verbose_name='组织名称', max_length=64)
    profile = models.CharField(max_length=256, blank=True, null=True, verbose_name='用户头像')
    orgIntro = models.TextField(verbose_name='组织简介',
                                null=True, blank=True, default='在这里介绍组织')
    password = models.CharField(verbose_name='密码', max_length=32)


class Policy(models.Model):
    bulk = models.TextField(verbose_name='主体', default='该政策是：')
    policyType = models.CharField(verbose_name='政策类型', max_length=16)
    timeStamp = models.CharField(verbose_name='时间戳-创建时间', max_length=32)
    source = models.CharField(verbose_name='来源', max_length=64)
    webLink = models.CharField(verbose_name='网页链接', max_length=256)
    cover = models.CharField(max_length=256, null=True, blank=True, verbose_name='封面')
    pic = models.CharField(max_length=256, null=True, blank=True, verbose_name='图片')
    theme = models.CharField(verbose_name='主题', max_length=256)


class Act(models.Model):
    bulk = models.TextField(verbose_name='主体内容')
    type = models.CharField(verbose_name='活动类型', max_length=32)
    timeStamp = models.CharField(verbose_name='时间戳-创建时间', max_length=32)
    theme = models.CharField(verbose_name='活动主题', max_length=256)
    pic = models.CharField(max_length=256, null=True, blank=True, verbose_name='图片')
    cover = models.CharField(max_length=256, null=True, blank=True, verbose_name='封面')


class Post(models.Model):
    theme = models.CharField(verbose_name='主题', max_length=256)
    bulk = models.TextField(verbose_name='主体内容')
    pic = models.CharField(max_length=256, blank=True, null=True, verbose_name='图片')
    timeStamp = models.CharField(verbose_name='时间戳-创建时间', max_length=32)
    schNo = models.CharField(verbose_name='学号', max_length=16)
    thumb = models.IntegerField(verbose_name='点赞量', default=0)


class Reply(models.Model):
    schNo = models.CharField(verbose_name='学号', max_length=16)
    bulk = models.TextField(verbose_name='主体内容')
    timeStamp = models.CharField(verbose_name='时间戳-创建时间', max_length=32)
    pic = models.CharField(max_length=256, blank=True, null=True, verbose_name='用户头像')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


class Volunteer(models.Model):
    name = models.CharField(verbose_name='名字', max_length=16)
    insit = models.CharField(verbose_name='书院', max_length=16)
    contact = models.CharField(verbose_name='联系方式', max_length=64)
    subject = models.CharField(verbose_name='学科', max_length=64)
    major = models.CharField(verbose_name='专业', max_length=64)
