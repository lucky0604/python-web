from django.utils import timezone

def random_nick_name():
  current = str(timezone.now()).split('.')[0].replace('-', '').replace(':', '').replace(' ', '')
  nick_name = 'User %s' % current
  return nick_name