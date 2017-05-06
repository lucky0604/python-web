import string
import random

# this couldn't be work, because in models.py, import utils
# from shortener.models import SoftURL

# shortcode generation
def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):

    """
    normal style

    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    """
    # the same as
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size = 6):
    new_code = code_generator(size = size)
    # if wanna use models, use instance.__class__
    SoftURL = instance.__class__
    qs_exists = SoftURL.objects.filter(shortcode = new_code).exists()

    return create_shortcode(size = size) if qs_exists else new_code
    """
    if qs_exists:
        return create_shortcode(size = size)
    return new_code
    """
