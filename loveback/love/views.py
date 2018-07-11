from datetime import datetime, timedelta
import re

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.core.urlresolvers import reverse

from functions.units import get_ticket
from love.models import User, UserTicketModel




def regist(request):
    #注册
    if request.method == 'GET':
        return render(request, 'regist.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        # if not User:
        #如果没注册过，就新注册
        if not all([username,password,password2,mobile]):
            msg = '请填写完整信息'
            return render(request,'regist.html',{'msg':msg})

        #密码加密
        if not re.findall(r'^1[34578]\d{9}$',mobile):
            msg = '请输入正确手机号'
            return render(request, 'regist.html', {'msg': msg})

        if not re.findall('^(?![A-Za-z]+$)(?![A-Z\\d]+$)(?![A-Z\\W]+$)'
                          '(?![a-z\\d]+$)(?![a-z\\W]+$)(?![\\d\\W]+$)\\S{6,20}$',password):
            msg = '请输入6到20位字母、数字、字符'
            return render(request, 'regist.html', {'msg': msg})

        password = make_password(password)
        User.objects.create(u_name=username,
                            u_password=password,
                            u_iphone=mobile)

        return HttpResponseRedirect(reverse('love:login'))
        # else:
        #     msg = '用户名已经存在'
        #     return render(request, 'regist.html', {'msg': msg})


def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(u_name=username).first()
        request.session['u_name'] = request.POST['username']
        if user:
            if check_password(password, user.u_password):

                #这里是用自带的验证密码用户
                ticket = get_ticket()
                response = HttpResponseRedirect(reverse('love:index'))
                out_time = datetime.now() + timedelta(days=1)

                response.set_cookie('ticket', ticket, expires=out_time)
                # 2. 保存ticket到服务端的user_ticket表中
                UserTicketModel.objects.create(user=user, out_time=out_time, ticket=ticket)
                #这里必须写HttpResponseRedirecet（reverse 才能实现重定向接口刷新
                return HttpResponseRedirect(reverse('love:index'))
            else:
                msg = '密码错误,请重新输入'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = '用户不存在'
            return render(request, 'login.html', {'msg': msg})

#登录成功
def index(request):

    username = request.session.get('u_name')
    return render(request, 'index.html', {'username': username})


def logout(request):
    if request.method == 'GET':
        #退出 返回登录界面
        response = HttpResponseRedirect(reverse('love:login'))
        response.delete_cookie('ticket')
        return render(request, 'index.html')
