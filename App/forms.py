from django import forms
from django.contrib import auth

from .models import *
from .other import my_md5
import re


# 注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=16,
        min_length=2,
        error_messages={
            'required':'用户名必须填写',
            'max_length': '用户名长度最长不超过16',
            'min_length': '用户名长度最少不低于2',
        }
    )

    phone = forms.CharField(
        required=True,
        max_length=11,
        min_length=11,
        error_messages={
            'required':'手机号必须填写',
            'max_length': '手机号长度为11位',
            'min_length': '手机号长度为11位',
        }
    )

    password = forms.CharField(
        required=True,
        max_length=18,
        min_length=6,
        error_messages={
            'required': '密码必须填写',
            'max_length': '密码长度最长不超过18',
            'min_length': '密码长度最少不低于6',
        }
    )
    #
    # password2 = forms.CharField(
    #     required=True,
    #     max_length=18,
    #     min_length=6,
    #     error_messages={
    #         'required': '重复密码必须填写',
    #         'max_length': '重复密码长度最长不超过18',
    #         'min_length': '重复密码长度最少不低于6',
    #     }
    # )

    vcode = forms.CharField(
        required=True,
        error_messages={
            'required': '验证码必须填写',
        }
    )



    def clean(self):
        username = self.cleaned_data.get('username')
        phone = self.cleaned_data.get('phone')
        # password = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')

        # 检测重复密码是否正确
        # if password != password2:
        #     raise forms.ValidationError({'password2': '2次密码不一致'})

        # 检测用户名是否已经注册过
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError({'username': '用户名已经存在'})

        # 检测手机号是否已经注册过
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError({'phone': '手机号已经存在'})

        # 检测手机号格式是否正确
        # if not re.match(r'^1[34578]\d{9}$',str(phone)):
        #     raise forms.ValidationError({'phone': '手机号格式不正确'})


        return self.cleaned_data


# 登录表单
class LoginForm(forms.Form):
    name = forms.CharField(
        required=True,
        error_messages={
            'required':'用户名/手机号 必须填写',
        }
    )

    password = forms.CharField(
        required=True,
        error_messages={
            'required': '密码必须填写',
        }
    )

    vcode = forms.CharField(
        required=True,
        error_messages={
            'required': '验证码必须填写',
        }
    )




    def clean(self):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')

        # 检测账号输入是否为手机号
        if re.match(r'^1[34578]\d{9}$', str(name)):
            phone = name
            users = User.objects.filter(phone=phone)
        else:
            username = name
            users = User.objects.filter(username=username)

        # 检测账号是否存在
        if not users.exists():
            raise forms.ValidationError({'name': '用户不存在'})
        # 检测密码是否正确
        elif users.first().password != my_md5(password):
            raise forms.ValidationError({'password': '用户名或密码错误'})

        # 添加user到数据
        self.cleaned_data['user'] = users.first()

        return self.cleaned_data



