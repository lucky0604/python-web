# custom authentication backend

from django.contrib.auth.models import User

class EmailAuthBackend(object):
    # authenticate using e-mail account
    def authenticate(self, username = None, password = None):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None


'''
django provides a simple way to define your own authentication backends. An authentication backend is a class that provides the following two methods:
authenticate()
get_user()

creating a custom authentication backend is as simple as writing a Python class that implements both methods
'''
