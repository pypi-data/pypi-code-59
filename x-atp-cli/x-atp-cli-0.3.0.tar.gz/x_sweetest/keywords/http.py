from copy import deepcopy
import requests
import json
from injson import check
from x_sweetest.globals import g
from x_sweetest.elements import e
from x_sweetest.log import logger
from x_sweetest.parse import data_format
from x_sweetest.utility import json2dict
from pathlib import Path
from requests_toolbelt.multipart.encoder import MultipartEncoder

path = Path('lib') / 'http_handle.py'
if path.is_file():
    from lib import http_handle
else:
    from x_sweetest.lib import http_handle


class Http:

    def __init__(self, step):
        # 获取 baseurl
        baseurl = e.get(step['page'] + '-' + 'baseurl', True)[1]
        if not baseurl:
            self.baseurl = ''
        else:
            if not baseurl.endswith('/'):
                baseurl += '/'
            self.baseurl = baseurl

        self.r = requests.Session()
        # 获取 headers
        self.headers_get = e.get(step['page'] + '-' + 'headers_get', True)[1]
        self.headers_post = e.get(step['page'] + '-' + 'headers_post', True)[1]


def get(step):
    request('get', step)


def post(step):
    request('post', step)


def put(step):
    request('put', step)


def patch(step):
    request('patch', step)


def delete(step):
    request('delete', step)


def options(step):
    request('options', step)


def request(kw, step):
    element = step['element']
    url = e.get(element)[1]
    if url.startswith('/'):
        url = url[1:]

    data = step['data']
    # 测试数据解析时，会默认添加一个 text 键，需要删除
    if 'text' in data and not data['text']:
        data.pop('text')

    _data = {}
    _data['headers'] = json2dict(data.pop('headers', '{}'))
    if data.get('cookies'):
        data['cookies'] = json2dict(data['cookies'])
    if kw == 'get':
        _data['params'] = json2dict(
            data.pop('params', '{}')) or json2dict(data.pop('data', '{}'))
    elif kw == 'post':
        if data.get('text'):
            _data['data'] = data.pop('text')
        else:
            _data['data'] = json2dict(data.pop('data', '{}'))
        _data['json'] = json2dict(data.pop('json', '{}'))
        _data['files'] = eval(data.pop('files', 'None'))
    elif kw in ('put', 'patch'):
        _data['data'] = json2dict(data.pop('data', '{}'))

    for k in data:
        for s in ('{', '[', 'False', 'True'):
            if s in data[k]:
                try:
                    data[k] = eval(data[k])
                except:
                    logger.warning('Try eval data failure: %s' % data[k])
                break
    expected = step['expected']
    expected['status_code'] = expected.get('status_code', None)
    expected['text'] = expected.get('text', None)
    json_str = expected.get('json', '{}')
    if json_str[0] == '[' and json_str[1] != ']':
        index = json_str.split(']')[0][1:]
        expected['json'] = json2dict(json_str[len(index) + 2:])
        expected['json_index'] = int(index)
    else:
        expected['json'] = json2dict(expected.get('json', '{}'))
    expected['cookies'] = json2dict(expected.get('cookies', '{}'))
    expected['headers'] = json2dict(expected.get('headers', '{}'))
    timeout = float(expected.get('timeout', 10))
    expected['time'] = float(expected.get('time', 0))

    if not g.http.get(step['page']):
        g.http[step['page']] = Http(step)
    http = g.http[step['page']]

    if kw == 'post':
        if http.headers_post:
            http.r.headers.update(eval(http.headers_post))
    else:
        if http.headers_get:
            http.r.headers.update(eval(http.headers_get))

    logger.info('URL: %s' % http.baseurl + url)

    # 处理 before_send
    before_send = data.pop('before_send', '')
    if before_send:
        _data, data = getattr(http_handle, before_send)(kw, _data, data)
    else:
        _data, data = getattr(http_handle, 'before_send')(kw, _data, data)

    if _data['headers']:
        for k in [x for x in _data['headers']]:
            if not _data['headers'][k]:
                del http.r.headers[k]
                del _data['headers'][k]
        http.r.headers.update(_data['headers'])

    if kw == 'get':
        r = getattr(http.r, kw)(http.baseurl + url,
                                params=_data['params'], timeout=timeout, **data)
        if _data['params']:
            logger.info(f'PARAMS: {_data["params"]}')

    elif kw == 'post':
        if 'form' in data:
            form_dict = json2dict(data['form'])
            try:
                if len(form_dict) == 1:
                    for form_k, form_v in form_dict.items():
                        form_name = form_k.split("/")[-1]
                        form_data = MultipartEncoder(fields={'file': (form_name, open(form_k, 'rb'), form_v)})
                        form_headers = {'Content-Type': form_data.content_type}
                        http.r.headers.update(form_headers)
                        r = getattr(http.r, kw)(http.baseurl + url, data=form_data, timeout=timeout)
            except:
                logger.exception("***form can be only one Key-value***")
        else:
            r = getattr(http.r, kw)(http.baseurl + url,
                                    data=_data['data'], json=_data['json'], files=_data['files'], timeout=timeout, **data)
        logger.info(f'BODY: {r.request.body}')

    elif kw in ('put', 'patch'):
        if 'binary' in data:
            binary_dict = json2dict(data['binary'])
            try:
                if len(binary_dict) == 1:
                    for binary_k, binary_v in binary_dict.items():
                        binary_headers = {'Content-Type': binary_v}
                        http.r.headers.update(binary_headers)
                        with open(binary_k, 'rb') as binary_f:
                            r = getattr(http.r, kw)(http.baseurl + url, data=binary_f, timeout=timeout)
            except:
                logger.exception("*** binary can be only one Key-value***")
        else:
            r = getattr(http.r, kw)(http.baseurl + url,
                                    data=_data['data'], timeout=timeout, **data)
        logger.info(f'BODY: {r.request.body}')

    elif kw in ('delete', 'options'):
        r = getattr(http.r, kw)(http.baseurl + url, timeout=timeout, **data)

    logger.info('status_code: %s' % repr(r.status_code))
    try:  # json 响应
        logger.info('response json: %s' % repr(r.json()))
    except:  # 其他响应
        logger.info('response text: %s' % repr(r.text))

    response = {'status_code': r.status_code, 'headers': r.headers,
                '_cookies': r.cookies, 'content': r.content, 'text': r.text}

    try:
        response['cookies'] = requests.utils.dict_from_cookiejar(r.cookies)
    except:
        response['cookies'] = r.cookies

    try:
        j = r.json()
        response['json'] = j
    except:
        response['json'] = {}

    # 处理 after_receive
    after_receive = expected.pop('after_receive', '')
    if after_receive:
        response = getattr(http_handle, after_receive)(response)
    else:
        response = getattr(http_handle, 'after_receive')(response)

    var = {}  # 存储所有输出变量

    if expected['status_code']:
        if str(expected['status_code']) != str(response['status_code']):
            raise Exception(
                f'status_code | EXPECTED:{repr(expected["status_code"])}, REAL:{repr(response["status_code"])}')

    if expected['text']:
        if expected['text'].startswith('*'):
            if expected['text'][1:] not in response['text']:
                raise Exception(f'text | EXPECTED:{repr(expected["text"])}, REAL:{repr(response["text"])}')
        else:
            if expected['text'] == response['text']:
                raise Exception(f'text | EXPECTED:{repr(expected["text"])}, REAL:{repr(response["text"])}')

    if expected['headers']:
        result = check(expected['headers'], response['headers'])
        logger.info('headers check result: %s' % result)
        if result['code'] != 0:
            raise Exception(
                f'headers | EXPECTED:{repr(expected["headers"])}, REAL:{repr(response["headers"])}, RESULT: {result}')
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('headers var: %s' % (repr(result['var'])))

    if expected['cookies']:
        logger.info('response cookies: %s' % response['cookies'])
        result = check(expected['cookies'], response['cookies'])
        logger.info('cookies check result: %s' % result)
        if result['code'] != 0:
            raise Exception(
                f'cookies | EXPECTED:{repr(expected["cookies"])}, REAL:{repr(response["cookies"])}, RESULT: {result}')
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('cookies var: %s' % (repr(result['var'])))

    if expected['json']:
        if 'json_index' in expected:
            result = check(expected['json'], response['json'][expected['json_index']])
        else:
            result = check(expected['json'], response['json'])
        logger.info('json check result: %s' % result)
        if result['code'] != 0:
            raise Exception(
                f'json | EXPECTED:{repr(expected["json"])}, REAL:{repr(response["json"])}, RESULT: {result}')
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('json var: %s' % (repr(result['var'])))

    if expected['time']:
        if expected['time'] < r.elapsed.total_seconds():
            raise Exception(f'time | EXPECTED:{repr(expected["time"])}, REAL:{repr(r.elapsed.total_seconds())}')

    output = step['output']
    # if output:
    #     logger.info('output: %s' % repr(output))

    for k, v in output.items():
        if v == 'status_code':
            g.var[k] = response['status_code']
            logger.info('%s: %s' % (k, repr(g.var[k])))
        elif v == 'text':
            g.var[k] = response['text']
            logger.info('%s: %s' % (k, repr(g.var[k])))
        elif k == 'json':
            sub_str = output.get('json', '{}')
            if sub_str[0] == '[':
                index = sub_str.split(']')[0][1:]
                sub = json2dict(sub_str[len(index) + 2:])
                result = check(sub, response['json'][int(index)])
            else:
                sub = json2dict(output.get('json', '{}'))
                result = check(sub, response['json'])
            # logger.info('Compare json result: %s' % result)
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('json var: %s' % (repr(result['var'])))
        elif k == 'cookies':
            sub = json2dict(output.get('cookies', '{}'))
            result = check(sub, response['cookies'])
            # logger.info('Compare json result: %s' % result)
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('cookies var: %s' % (repr(result['var'])))
    if var:
        step['_output'] += '\n||output=' + str(var)
