# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from bizerror.base import BizErrorBase
from bizerror.base import set_error_message

# Created: 2020-07-19 15:45:25.144000
# WARNING! All changes made in this file will be lost!


class OK(BizErrorBase):
    CODE = 0
set_error_message("en", 0, "OK")
set_error_message("zh-Hans", 0, "OK")

class SysError(BizErrorBase):
    CODE = 1001000000
set_error_message("en", 1001000000, "System Error")
set_error_message("zh-Hans", 1001000000, "系统异常")

class UndefinedError(SysError):
    CODE = 1001000001
set_error_message("en", 1001000001, "Unknown Error")
set_error_message("zh-Hans", 1001000001, "未定义的异常")

class DatabaseError(SysError):
    CODE = 1001000002
set_error_message("en", 1001000002, "System Error")
set_error_message("zh-Hans", 1001000002, "服务器异常")

class CacheError(SysError):
    CODE = 1001000003
set_error_message("en", 1001000003, "System Error")
set_error_message("zh-Hans", 1001000003, "服务器异常")

class MessageQueueError(SysError):
    CODE = 1001000004
set_error_message("en", 1001000004, "System Error")
set_error_message("zh-Hans", 1001000004, "服务器异常")

class AnotherServiceError(SysError):
    CODE = 1001000005
set_error_message("en", 1001000005, "System Error")
set_error_message("zh-Hans", 1001000005, "服务器异常")

class HttpError(BizErrorBase):
    CODE = 1001010000
set_error_message("en", 1001010000, "Http Error.")
set_error_message("zh-Hans", 1001010000, "HTTP请求相关异常。")

class RequestExpired(HttpError):
    CODE = 1001010001
set_error_message("en", 1001010001, "Request expired.")
set_error_message("zh-Hans", 1001010001, "请求已过期！")

class NotSupportedHttpMethod(HttpError):
    CODE = 1001010002
set_error_message("en", 1001010002, "Not supported http method")
set_error_message("zh-Hans", 1001010002, "不支持的请求方法！")

class ConfigError(BizErrorBase):
    CODE = 1001020000
set_error_message("en", 1001020000, "Config error.")
set_error_message("zh-Hans", 1001020000, "配置相关异常。")

class MissingConfigItem(ConfigError):
    CODE = 1001020001
set_error_message("en", 1001020001, "Missing config item: {item}.")
set_error_message("zh-Hans", 1001020001, "缺少必要的配置项：{item}。")

class DataError(BizErrorBase):
    CODE = 1001030000
set_error_message("en", 1001030000, "Data error.")
set_error_message("zh-Hans", 1001030000, "数据相关异常。")

class TargetNotFound(DataError):
    CODE = 1001030001
set_error_message("en", 1001030001, "Target not found.")
set_error_message("zh-Hans", 1001030001, "没有找到目标对象！")

class AuthError(BizErrorBase):
    CODE = 1001040000
set_error_message("en", 1001040000, "Auth error.")
set_error_message("zh-Hans", 1001040000, "认证相关异常。")

class AccountLockedError(AuthError):
    CODE = 1001040001
set_error_message("en", 1001040001, "Account locked.")
set_error_message("zh-Hans", 1001040001, "帐号被锁定，请联系管理员！")

class AccountTemporaryLockedError(AuthError):
    CODE = 1001040002
set_error_message("en", 1001040002, "Account temporary locked.")
set_error_message("zh-Hans", 1001040002, "登录失败次数超过上限，帐号被临时锁定！")

class UserPasswordError(AuthError):
    CODE = 1001040003
set_error_message("en", 1001040003, "User not exist or wrong password.")
set_error_message("zh-Hans", 1001040003, "帐号或密码错误，请重试！")

class AppAuthFailed(AuthError):
    CODE = 1001040004
set_error_message("en", 1001040004, "App auth failed.")
set_error_message("zh-Hans", 1001040004, "应用认证失败！")

class TsExpiredError(AuthError):
    CODE = 1001040005
set_error_message("en", 1001040005, "Timestamp expired.")
set_error_message("zh-Hans", 1001040005, "时间戳已失效。")

class AccountDisabledError(AuthError):
    CODE = 1001040006
set_error_message("en", 1001040006, "Account disabled.")
set_error_message("zh-Hans", 1001040006, "帐号已禁用，请联系管理员！")

class AccountStatusError(AuthError):
    CODE = 1001040007
set_error_message("en", 1001040007, "Bad account status.")
set_error_message("zh-Hans", 1001040007, "帐号状态异常，请联系管理员处理！")

class AccountRemovedError(AuthError):
    CODE = 1001040008
set_error_message("en", 1001040008, "Account removed.")
set_error_message("zh-Hans", 1001040008, "帐号已删除！")

class LoginRequired(AuthError):
    CODE = 1001040009
set_error_message("en", 1001040009, "Login required.")
set_error_message("zh-Hans", 1001040009, "请先登录！")

class AccessDenied(AuthError):
    CODE = 1001040010
set_error_message("en", 1001040010, "Access denied.")
set_error_message("zh-Hans", 1001040010, "禁止访问！")

class TypeError(BizErrorBase):
    CODE = 1001050000
set_error_message("en", 1001050000, "Type error.")
set_error_message("zh-Hans", 1001050000, "数据类型相关异常。")

class CastToIntegerFailed(TypeError):
    CODE = 1001050001
set_error_message("en", 1001050001, "Cast to integer value failed on field {field}.")
set_error_message("zh-Hans", 1001050001, "字段{field}转化整数型数据失败！")

class CastToFloatFailed(TypeError):
    CODE = 1001050002
set_error_message("en", 1001050002, "Cast to float value failed on field {field}.")
set_error_message("zh-Hans", 1001050002, "字段{field}转化浮点数型数据失败！")

class CastToNumbericFailed(TypeError):
    CODE = 1001050003
set_error_message("en", 1001050003, "Cast to numberic value failed on field {field}.")
set_error_message("zh-Hans", 1001050003, "字段{field}转化数值型数据失败！")

class CastToBooleanFailed(TypeError):
    CODE = 1001050004
set_error_message("en", 1001050004, "Cast to boolean value failed on field {field}.")
set_error_message("zh-Hans", 1001050004, "字段{field}转化布尔型数据失败！")

class CastToStringFailed(TypeError):
    CODE = 1001050005
set_error_message("en", 1001050005, "Cast to string value failed on field {field}.")
set_error_message("zh-Hans", 1001050005, "字段{field}转化字符串型数据失败！")

class ParseJsonError(TypeError):
    CODE = 1001050006
set_error_message("en", 1001050006, "Parse json error.")
set_error_message("zh-Hans", 1001050006, "Json转化异常！")

class NotSupportedTypeToCast(TypeError):
    CODE = 1001050007
set_error_message("en", 1001050007, "Not supported type to cast.")
set_error_message("zh-Hans", 1001050007, "该类型不支持转化！")

class ParamError(BizErrorBase):
    CODE = 1001060000
set_error_message("en", 1001060000, "Param error.")
set_error_message("zh-Hans", 1001060000, "参数相关异常。")

class MissingParameter(ParamError):
    CODE = 1001060001
set_error_message("en", 1001060001, "Missing parameter: {parameter}.")
set_error_message("zh-Hans", 1001060001, "必要参数缺失：{parameter}。")

class BadParameter(ParamError):
    CODE = 1001060002
set_error_message("en", 1001060002, "Bad parameter: {parameter}.")
set_error_message("zh-Hans", 1001060002, "参数值有误：{parameter}。")

class BadParameterType(ParamError):
    CODE = 1001060003
set_error_message("en", 1001060003, "Bad parameter type: {parameter}.")
set_error_message("zh-Hans", 1001060003, "参数类型有误：{parameter}。")

class FormError(BizErrorBase):
    CODE = 1001070000
set_error_message("en", 1001070000, "Form error.")
set_error_message("zh-Hans", 1001070000, "表单相关异常。")

class CaptchaOnlyAllowedOnce(FormError):
    CODE = 1001070001
set_error_message("en", 1001070001, "Captcha only allowed one time use.")
set_error_message("zh-Hans", 1001070001, "验证码不允许重复使用！")

class CaptchaValidateFailed(FormError):
    CODE = 1001070002
set_error_message("en", 1001070002, "Captcha validate failed.")
set_error_message("zh-Hans", 1001070002, "图片验证码校验失败！")

class RepeatedlySubmitForm(FormError):
    CODE = 1001070003
set_error_message("en", 1001070003, "Please do not submit a form repeatedly.")
set_error_message("zh-Hans", 1001070003, "请不要重复提交表单！")

class LogicError(BizErrorBase):
    CODE = 1001080000
set_error_message("en", 1001080000, "Logic error.")
set_error_message("zh-Hans", 1001080000, "业务逻辑相关异常。")
