import os


def RECAPTCHA_V3_SITE():
    return os.environ['BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE']


def RECAPTCHA_V3_SECRET():
    return os.environ['BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET']


def RECAPTCHA_V3_SCORE():
    return float(os.environ.get('BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE', "0.5"))


def RECAPTCHA_V3_DISABLE():
    return int(os.environ.get('BUKDJANGO_CAPTCHA_RECAPTCHA_V3_DISABLE', 0))
