import logging

import requests
from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from bukdjango_captcha.recaptcha_v3 import secrets

logger = logging.getLogger(__name__)


class ReCaptchaV3Input(widgets.HiddenInput):
    template_name = 'bukdjango_captcha/recaptcha_v3/recaptcha_v3_input.html'

    def value_from_datadict(self, data, files, name):
        return data.get('g-recaptcha-response', None)


class RecaptchaV3Field(forms.CharField):

    def __init__(self, **kwargs):
        kwargs.setdefault('widget', ReCaptchaV3Input())
        super().__init__(**kwargs)

    def clean(self, value):

        if secrets.RECAPTCHA_V3_DISABLE():
            return

        try:
            r = requests.post(
                url='https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': secrets.RECAPTCHA_V3_SECRET(),
                    'response': value,
                },
                timeout=10,
            )
            r.raise_for_status()

        except requests.RequestException as e:
            logger.exception(e)
            raise forms.ValidationError(
                _('Please try again later.'),
                code='requests_exception',
            )

        data = r.json()
        logger.info(data)

        if not data['success'] or data['score'] < secrets.RECAPTCHA_V3_SCORE():
            logger.error(data)
            raise forms.ValidationError(
                _('Are you a robot?'),
                code='recaptcha_v3_invalid',
            )
