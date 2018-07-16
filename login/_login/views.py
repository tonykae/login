#coding:utf-8
from django.shortcuts import render,redirect
from models import *
# Create your views here.
def index(request):
    return render(request,'_login/index.html')

def signup(request):

    return render(request,'_login/signup.html')

def signup_hander(request):
    name = request.POST['uname']
    password = request.POST['upassword']
    # context = {'name':name,
    #            'passwd':password
    #            }

    if User1Info.userset.checkname(name):
        return render(request, '_login/signup_hander2.html')
    else:
        user = User1Info.userset.increase(name, password)
        return render(request, '_login/signup_hander.html')
def login(request):
    return render(request,'_login/login.html')

def login_hander(request):
    name = request.POST['uname']
    password = request.POST['upassword']
    temp = User1Info.userset.login(name,password)

    str1 = "登陆成功！"
    str2 = "用户名或密码错误"
    str3 = "用户名不存在"
    if temp == 1:
        context = {
            'str':str1,
            'name':name,
        }
    if temp == 2:
        context = {'str':str2}

    if temp == 3:
        context = {'str':str3}

    return render(request,'_login/login_hander.html',context)