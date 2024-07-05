from app01 import models
from django import forms
from django.core.validators import ValidationError
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=2, label='用户名')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'})
        # }


class PrettyModelForm(BootStrapModelForm):
    # 引入正则，以表明要求的格式，添加校验规则
    # mobile = forms.CharField(
    #     label='手机号',
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    # )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = ['level']

    # 另一种判断格式的方式，钩子方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 手机号不能重复
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        if len(txt_mobile) != 11:
            raise ValidationError('格式错误')
        return txt_mobile


class PrettyModelEditForm(BootStrapModelForm):
    mobile = forms.CharField(
        # disabled=True,
        label='手机号',
        # validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        # 不允许更改电话号
        model = models.PrettyNum
        fields = '__all__'

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 手机号不能重复，且在编辑过程中注意排除这一项id
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        if len(txt_mobile) != 11:
            raise ValidationError('格式错误')
        return txt_mobile
