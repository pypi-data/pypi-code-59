from django import template
from bukdjango_captcha.recaptcha_v3 import secrets

register = template.Library()


@register.inclusion_tag('bukdjango_captcha/recaptcha_v3/recaptcha_v3_script.html')
def recaptcha_v3_script(site_key=None):
    return {
        'RECAPTCHA_V3_SITE': site_key or secrets.RECAPTCHA_V3_SITE(),
    }


@register.inclusion_tag('bukdjango_captcha/recaptcha_v3/recaptcha_v3_run.html')
def recaptcha_v3_run(site_key=None, action_name='submit'):
    return {
        'RECAPTCHA_V3_SITE': site_key or secrets.RECAPTCHA_V3_SITE(),
        'ACTION_NAME': action_name,
    }
