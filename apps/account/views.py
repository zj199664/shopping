import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader
from django.core.cache import cache
from itsdangerous import URLSafeSerializer
from apps.account.models import UserProfile
from shopping import settings


# 登录
def login_view(request):
    if request.method == 'GET':
        redirect_url = request.GET.get('next')
        return render(request, 'login.html', {'next': redirect_url})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user:
            # 判断用户是否激活
            if user.is_active:
                # 记住用户状态
                login(request, user)
                if redirect_url:
                    # 返回之前的页面
                    return redirect(redirect_url)
                else:
                    # 返回首页
                    return redirect('/')
            else:
                # 表示用户被禁用
                return render(request, 'login.html', {'msg': '账户已经被锁定，请于管理员联系'})
        else:
            # 登录失败
            return render(request, 'login.html', {'msg': '账号或密码错误'})


# 注册
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        password = request.POST.get('password')
        verity_password = request.POST.get('verity_password')
        email = request.POST.get('email')
        if not re.match('(^[a-zA-Z0-9_-]{4,16}$)', username):
            return render(request, 'register.html', {'msg': '用户名不符合规范'})
        # 查询用户是否存在
        if user.exists():
            return render(request, 'register.html', {'msg': '用户名已存在'})
        # 判断两次密码是否一致
        if password != verity_password:
            return render(request, 'register.html', {'msg': '两次密码不一致'})
        # 正则验证密码是否符合规范
        if not re.match('(^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$)', password):
            return render(request, 'register.html', {'msg': '密码不符合规范'})
        # 正则验证邮箱是否符合规范
        if not re.match('(^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$)', email):
            return render(request, 'register.html', {'msg': '邮箱不符合规范'})
        # 用户注册成功
        user = User.objects.create_user(username=username, password=password, email=email, is_active=0)
        user_profile = UserProfile( user_id=user.id)
        user_profile.save()
        if user:
            auth_s = URLSafeSerializer(settings.SECRET_KEY, 'auth')
            token = auth_s.dumps({'uid': user.id})
            cache.set(token, user.id, timeout=10 * 60)
            active_url = f'http://127.0.0.1:8000/account/active/?token={token}'
            content = loader.render_to_string('mail.html',
                                              request=request,
                                              context={'username': username, 'active_url': active_url})
            send_active_mail(subject='电影网激活邮件', content=content, to=[email])
            return redirect('/')


# 注销
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


# 更新
@login_required
def update_view(request):
    return


def active_account(request):
    # uid = request.GET.get('id')
    token = request.GET.get('token')
    uid = cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return redirect('/')
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询user对象
        return redirect('/')


# 发送邮件
def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )
