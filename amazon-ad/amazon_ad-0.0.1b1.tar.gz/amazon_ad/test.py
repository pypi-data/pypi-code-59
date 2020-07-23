# -*- coding: utf-8 -*-
# Authored by: Josh (joshzda@gmail.com)
import requests

from client.service import ZADServiceClient, ZADProfileClient
from client.auth import ZADAuthClient

client_id = 'amzn1.application-oa2-client.5f22ade077114ef980883e2045a2fde0'
client_secret = '1ac684981fd46f98752ac47929606cb1587a42ed1045de7f10a2391fd498769d'

access_token = 'Atza|IwEBIIg22gm72ULsYKegh702k74ZERq3MRIETxTa9pN5I_b4uG-BActSZTRD2w5ZomvkVn3OUfHXHgGr77rguMGnpu1z7K9fkCUsSIPDyyHjKC_LEXFpixJLLTg_6Kaio7ZWd-BzaOLW0YbYiIhNlJrXN1BvsniCxBqa9j3w_mAD0td8nOGSZQRLTGhRrMxKHDFiMqBu8Sde0kaX934cy4U29KgMGEsGHbsWoZpNef7mCLEhMuZtNy7mHcDDP9C_KOf6RZKM3c2tJj_BRud35-Ip8EARBOTcPHhH5-ysck9eUfJWyiNT6gXZMh5KZqDIQ21SopgPD8cFcHOBCzKVVhSJQjOh0mYRVtWy0QArxGilfGh10Vcfzc1426HGlxKsGJS8SzeAxts3WVwrZ4zyPIW__5N4g7CreMsAfhuGsywxk_HWB-TowhW-vEvDibEsQ8Oy5CU'


def refresh_access_token():
    refresh_token = 'Atzr|IwEBIAqVizlqGLRyEYDrjc4Nj7jQxbPh7yUvXxt7Kal0cXGgpKCk_cs93eMFeHdZgRNmtm1cimC4as6LEw4wJgIClRboOQ9bTL4ACkdnGoj50FZmW89EO9dQI41iH3iOkfObZTC8kyHowmwlj2ETKkGdXXeIunJj8u7FF_o44VbITAXybUuIJIN6k3cuvb2MSxxpOgdtUeRG-nmxV9e9ouIEopYK1M4gI4oH1gLadX_5AURiJDUcudDmY_nGu7fAvi8jhRsarjz4Y7fTCSm2Ijkk10uzHixHMJC7Qjqrh-7soJ0VLkoyO27gcDLzL4DWNyUpaaPvPeoAyAEvQUr-QYY1uVPEXhbOeGSVqXcegFJDMcEpl_w1HqqZPNAjAD9LTBkHvkACg8LwWfMzuh3WpAi0Hmo6SdbrKA2r7mrmZC3lH2YQQg'
    auth_client = ZADAuthClient(client_id, client_secret, 'SANDBOX')
    res = auth_client.token.refresh_token(refresh_token)
    print(res)

def profile():
    client = ZADProfileClient(client_id, access_token, country="SANDBOX")
    a = client.profiles.list()
    print(a)

def test():

    # client = ZADServiceClient(client_id, access_token, country="SANDBOX")
    # a = client.profiles.retrieve('4358504360586791')
    # print(a)

    client = ZADServiceClient(client_id, access_token, profile_id='4358504360586791', country="SANDBOX")
    a = client.sb_report.queries('20200720')
    # a = client.report_get.get_report('amzn1.clicksAPI.v1.m1.5F18F3C3.b2fffb10-7796-46ef-bbee-654c94a84717')
    # a = client.report_download.download('https://advertising-api-test.amazon.com/v1/reports/amzn1.clicksAPI.v1.m1.5F18F3C3.b2fffb10-7796-46ef-bbee-654c94a84717/download')

    print(a)

refresh_access_token()