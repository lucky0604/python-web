from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from users.models import Message, EmailVerifyCode
# from utils.email_send import send_password_email
from django.views.generic import View
from django.utils import timezone
from .models import UserProfile
from django.db.models import Q
from .forms import *
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.
__all__ = [
    'RegisterView',
    'LoginView',
    'LogoutView',
    'PasswordWord'
]

class CustomBackend(ModelBackend):
    '''
    customize auth check
    '''
    def authenticate(self, username = None, password = None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email = username))
            if user.check_password(password):
                return user
            else:
                return None
        except Exception:
            return None

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)  # 验证传递过来的参数
        if register_form.is_valid():
            email = request.POST.get('email', '')   # 获取邮箱
            try:
                UserProfile.objects.get(email = email)  # 如果邮箱已存在
                return render(request, 'register.html', {'errors': '邮箱%s已存在' % email})
            except ObjectDoesNotExist:
                password = request.POST.get('password', '') #获取密码
                retype_password = request.POST.get('retype_password', '')
                if password == retype_password:
                    UserProfile.objects.create(username = email, email = email, password = make_password(password))
                    Message.objects.create(body = '用户 %s 于 %s 注册成功' % (email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))
                else:
                    errors = '两次密码不一致'
                    return render(request, 'register.html', {'errors': errors})
        else:
            return render(request, 'register.html', {'errors': register_form.errors})

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        '''
        验证用户是否可以成功登陆
        '''
        login_form = LoginForm(request.POST)        # FORM验证传过来的值是否合法
        if login_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = authenticate(username = email, password = password)      # 验证用户名和密码
            if user is not None:    # 如果用户名和密码匹配
                if user.is_active:  # 如果用户是激活状态
                    login(request, user)    # 把Session和Cookie写入request
                    if user.is_superuser:
                        return HttpResponseRedirect(reverse('admin:dashboard'))     # 返回首页
                    else:
                        return HttpResponseRedirect(reverse('index'))       # 返回首页

                else:
                    return render(request, 'login.html', {'errors': '用户尚未激活'})
            else:
                return render(request, 'login.html', {'errors': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'errors': login_form.errors})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

class PasswordView(View):
    def get(self, request):
        code = request.GET.get('code': '')
        if code:
            try:
                EmailVerifyCode.objects.get(code = code)
                return render(request, 'password.html', {'code': code, 'flag': True})
            except EmailVerifyCode.DoesNotExist:
                return HttpResponse('重置密码链接已失效')
        else:
            return render(request, 'password.html')

    def post(self, request):
        email = request.POST.get('email', '')
        try:
            UserProfile.objects.get(email = email)
            result = send_password_email(email = email)
            if result:
                return HttpResponse('重置密码已发送您邮箱，请注意查收')
            return HttpResponse('用户不存在')
        except UserProfile.DoesNotExist:
            return HttpResponse('用户不存在')

class RestPasswordView(View):
    def post(self, request):
        code = request.POST.get('code')
        if code:
            rest_form = RestPasswordForm(request.POST)
            if rest_form.is_valid():
                password = request.POST.get('password', '')     # 获取密码
                retype_password = request.POST.get('retype_password', '')   # 确认密码
                if password = retype_password:
                    emailVerify = EmailVerifyCode.objects.get(code = code)
                    email = emailVerify.email
                    user = UserProfile.objects.get(email = email)
                    user.password = make_password(password)
                    user.save()
                    emailVerify.delete()
                    Message.objects.create(body = '用户 %s 于 %s 修改了密码' % (email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse('两次密码不一致')
            else:
                return HttpResponse(rest_form.errors)
        else:
            admin_password_form = AdminRestPasswordForm(request.POST)
            if admin_password_form.is_valid():
                oldPassword = request.POST.get('oldPassword')
                newPassword = request.POST.get('newPassword')
                retypePassword = request.POST.get('retypePassword')
                user = authenticate(username = request.user.email, password = oldPassword)
                if newPassword == retypePassword and user:
                    user.password = make_password(newPassword)
                    user.save()
                    logout(request)
                    Message.objects.create(body = '用户 %s 于 %s 通过后台修改了密码' % (request.user.email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse('请确保两次密码相同')
            else:
                return HttpResponse(admin_password_form.errors)
