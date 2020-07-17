# -*- coding: utf-8 -*-
"""
    picbed-smtp
    ~~~~~~~~~~~

    Send email with third smtp server.

    :copyright: (c) 2020 by staugur.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

__version__ = '0.1.0'
__author__ = 'staugur <staugur@saintic.com>'
__hookname__ = 'picbed-smtp'
__description__ = '通过SMTP服务发送邮件'

from utils.tool import Mailbox, mail_pat
from flask import g

intpl_emailsetting = '''
<div class="layui-col-xs12 layui-col-sm12 layui-col-md12">
    <fieldset class="layui-elem-field">
        <legend>SMTP</legend>
        <div class="layui-field-box">
            <div class="layui-form-item">
                <div class="layui-inline">
                    <label class="layui-form-label" style="width: auto;">发件人</label>
                    <div class="layui-input-inline">
                        <input type="text" name="email_smtp_from"
                            value="{{ g.site.email_smtp_from }}" placeholder="发件邮箱地址"
                            autocomplete="off" class="layui-input">
                    </div>
                </div>
                <div class="layui-inline">
                    <label class="layui-form-label" style="width: auto;">密码</label>
                    <div class="layui-input-inline">
                        <input type="password" name="email_smtp_passwd"
                            value="{{ g.site.email_smtp_passwd }}" placeholder="邮箱授权码或密码"
                            autocomplete="off" class="layui-input">
                    </div>
                </div>
                <div class="layui-inline">
                    <label class="layui-form-label" style="width: auto;">SMTP</label>
                    <div class="layui-input-inline">
                        <input type="text" name="email_smtp_server"
                            value="{{ g.site.email_smtp_server }}" placeholder="SMTP服务器域名:端口(默认25)"
                            autocomplete="off" class="layui-input" list="smtps">
                        <datalist id="smtps">
                            <option value="smtp.qq.com:465">QQ邮箱</option>
                            <option value="smtp.exmail.qq.com:465">腾讯企业邮箱</option>
                            <option value="smtp.163.com:995">网易163邮箱</option>
                            <option value="smtp.ym.163.com:994">网易免费企业邮箱</option>
                            <option value="smtp.gmail.com:465">Gmail</option>
                        </datalist>
                    </div>
                </div>
            </div>
        </div>
    </fieldset>
</div>
'''


def sendmail(subject, message, to_addr):
    res = dict(code=1)
    from_name = g.cfg.email_from_name or g.cfg.title_name or "picbed"
    smtp_server = g.cfg.email_smtp_server
    smtp_from = g.cfg.email_smtp_from
    smtp_passwd = g.cfg.email_smtp_passwd
    if smtp_server and smtp_from and mail_pat.match(smtp_from) and smtp_passwd:
        if ":" in smtp_server:
            smtp_server, smtp_port = smtp_server.split(":")
        else:
            smtp_port = 25
        try:
            smtp_port = int(smtp_port)
        except (ValueError, TypeError):
            res.update(code=3, msg="Parameter error")
        else:
            smtp = Mailbox(smtp_from, smtp_passwd, smtp_server, smtp_port)
            res = smtp.send(subject, message, to_addr, from_name)
    else:
        res.update(code=2, msg="Parameter error")
    res["method"] = "smtp"
    return res
