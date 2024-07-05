"""tiny_shell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from stu.views import stuaccount, policy, act, post, \
    stuinfo_1, volunteer, reply, ChangeMsg, img, search, decode_token, thumb, userinfo

urlpatterns = [
    # path('admin/', admin.site.urls),
    # jwt登录
    path('shells/login/', stuinfo_1.ProLoginView.as_view()),
    path('shells/info/', stuinfo_1.ProInfoView.as_view()),

    # 三类群体注册
    path('stu/register/', stuaccount.stu_register),  # 学生注册
    path('soldier/register/', stuaccount.soldier_register),  # 大学生士官注册
    path('org/register/', stuaccount.org_register),

    # 政策相关
    path('policy/add/', policy.policy_send),
    path('policy/list/', policy.policy_list),

    # 活动相关
    path('act/add/', act.act_send),
    path('act/list/', act.act_list),

    # 帖子相关
    path('post/add/', post.post_add),
    path('post/list/', post.post_list),
    path('post/delete/', post.post_delete),

    # 志愿者相关
    path('volunteer/add/', volunteer.volunteer_add),
    path('volunteer/list/', volunteer.volunteer_list),

    # 回复相关
    path('reply/add/', reply.reply_add),

    # msg_change
    path('stu/msg/change', ChangeMsg.StuMsg_edit),
    path('soldier/msg/change', ChangeMsg.SoldierMsg_edit),
    path('org/msg/change', ChangeMsg.OrgMsg_edit),

    # 上传图片，处理图片，更新图片用
    path('add/stu/image/', img.add_stu_image),

    # 搜索
    path('search/list/', search.search_list),

    # 图片上传
    path('pic/upload/', img.upload),

    # token
    path('decode/token/', decode_token.decode_token),

    # thumb
    path('thumb/good/', thumb.thumb),

    # stu_info
    path('stu/info/', userinfo.stu_info),
    path('soldier/info/', userinfo.soldier_info),
    path('org/info/', userinfo.org_info),

    # profile->info
    path('profile/info/', userinfo.profile_to_info),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
