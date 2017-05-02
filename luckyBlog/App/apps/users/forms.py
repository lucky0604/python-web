from django import forms

__all__ = [
    'RegisterForm',
    'LoginForm',
    'ResetPasswordForm',
    'AdminResetPasswordForm'
]

class RegisterForm(forms.Form):
    '''
    check regist form
    '''
    email = forms.EmailField(required = True)
    password = forms.CharField(required = True, min_length = 5)
    retype_password = forms.CharField(required = True, min_length = 5)
    

class LoginForm(forms.Form):
    '''
    check login form
    '''
    email = forms.CharField(required = True, max_length = 150)
    password = forms.CharField(required = True, max_length = 128)

class ResetPasswordForm(forms.Form):
    code = forms.CharField()
    password = forms.CharField(required = True, min_length = 5)
    retype_password = forms.CharField(required = True, min_length = 5)

class AdminResetPasswordForm(forms.Form):
    oldPassword = forms.CharField(required = True)
    newPassword = forms.CharField(required = True, min_length = 5)
    retypeNewPassword  =forms.CharField(required = True, min_length = 5)
