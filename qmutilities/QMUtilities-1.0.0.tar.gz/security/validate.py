from flask import request, abort, url_for
from security import secret_manager
import json
from pymemcache.client import base
import base64
from flask import jsonify


class ValidateHeader:
    @staticmethod
    def check_whitelisting(ip_list):
        """
        checks the IP if it belongs to the input range, otherwise it throws HTTPErr:403 error
        :return:
        """

        # To avoid unnecessary database queries, ignore the IP check for
        # requests for static files
        if request.path.startswith(url_for('static', filename='')):
            return

        # Some static files might be served from the root path (e.g.
        # favicon.ico, robots.txt, etc.). Ignore the IP check for most
        # common extensions of those files.
        ignored_extensions = ('ico', 'png', 'txt', 'xml')
        if request.path.rsplit('.', 1)[-1] in ignored_extensions:
            return

        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        if ip:
            print("Incoming request from IP: {}".format(ip))
            if ip not in ip_list:
                abort(403, jsonify({'message': 'Forbidden Access: {} Not an authorized IP'.format(ip),
                                    'status_code': 403}))
        else:
            return jsonify({'Exception': "AuthFailure",
                            'message': 'No IP found in RequestHeader,Please check Nginx config or header of the request',
                            'status_code': '424'})

    @staticmethod
    def check_okta_token(**kwargs):

        if request.method == "POST":
            return jsonify({'Exception': "AuthFailure",
                            'message': 'No Authorization header provided.',
                            'status_code': '424'})

        if request.headers.__contains__('Authentication'):
            okta_auth_header = request.headers['Authentication']
            if ValidateHeader.base64_encode(okta_auth_header):
                assert_id = base64.b64decode(okta_auth_header).split(':')[0]
            else:
                assert_id = okta_auth_header.split(' ')[3].split(':')[1]

            memcache_key = "assert:" + assert_id

            if 'SECRET_NAME' in kwargs.keys():
                cache_json = json.loads(secret_manager.get_secret(kwargs['SECRET_NAME']))
                aws_elastic_cache_hostname = cache_json['elastic_cache_hostname']
                port = cache_json['port']

            else:
                aws_elastic_cache_hostname = kwargs['MEMCACHE_HOST']
                port = kwargs['MEMCACHE_PORT']
            client = base.Client((aws_elastic_cache_hostname, int(port)))

            if not client.get(memcache_key):
                abort(403, jsonify({'message': 'Forbidden Access: Request not from an authorized user',
                                    'status_code': 403}))

    @staticmethod
    def base64_encode(token):

        if len(token) % 4 != 0:  # check if multiple of 4
            while len(token) % 4 != 0:
                token = token + "="
            decoded_token = base64.b64decode(token)
        else:
            decoded_token = base64.b64decode(token)
        if token == base64.b64encode(decoded_token):
            return True
        else:
            return False
