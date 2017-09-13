# -*- coding: utf-8 -*-
import json
import time
import hmac
import base64
import hashlib
import requests
# open_api_ip = '10.230.20.181'
# open_api_ip = '10.253.1.115'
open_api_ip = '192.168.218.35'
open_api_host = 'openapi.easyops-only.com'

def get_the_key():
    cmdb_api_url = 'http://%s/user/apikey' % open_api_ip
    headers = {'org': '1021', 'user': 'easyops', 'Host': 'cmdb.easyops-only.com'}
    resp = requests.get(cmdb_api_url, headers=headers)
    data = {}
    if resp.status_code == 200:
        data = resp.json()

    ACCESS_KEY = data.get('data').get('access_key')
    SECRET_KEY = data.get('data').get('secret_key')

    return ACCESS_KEY,SECRET_KEY

def open_api_requests(method, url, data, headers):
    if method == 'GET':
        resp = requests.get(url, params=data, headers=headers)
    elif method == 'POST':
        resp = requests.post(url, data=data, headers=headers)

    if resp.status_code == 200:
        return resp.json()

    return {}


def generate_signature(method, uri, params, content_type, data, request_time, access_key, secret_key):

    method = method.upper()
    # 对 params 进排序, 然后组合为一串 key + value 的string
    params_str = ''
    if method == 'GET' and params:
        params_str = ''.join([ '%s%s' % (key, params[key]) for key in sorted(params.keys()) ])

    # Content-MD5
    content_md5 = ''
    if method == 'POST' and data:
        m = hashlib.md5()
        m.update(json.dumps(data).encode('utf-8'))
        content_md5 = m.hexdigest()

    # 组合 str
    str_sign = str('\n'.join([
        method,
        uri,
        params_str,
        content_type,
        content_md5,
        str(request_time),
        access_key
    ]))

   # print type(str_sign)
    #print str_sign
    signature = hmac.new(str(secret_key), str_sign, hashlib.sha1).hexdigest()

    return signature


def do_api_with_openapi(method, uri, access_key, secret_key, data={}):
    url = 'http://{0}{1}'.format(open_api_ip, uri)
    headers = {
        'Host': open_api_host,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    request_time = int(time.time())
    signature = generate_signature(method=method,
                                   uri=uri,
                                   params=data,
                                   content_type=headers.get('Content-Type'),
                                   data=data,
                                   request_time=str(request_time),
                                   access_key=access_key,
                                   secret_key=secret_key)

    #print signature

    data.update({
        "accesskey": access_key,
        "signature": signature,
        "expires": str(request_time)
    })

    return open_api_requests(method, url, data, headers)

def get_monitor_info():
    (ACCESS_KEY, SECRET_KEY) = get_the_key()
    uri = '/cmdb/object/instance/list/HOST'
    params = {
        # 'businesses:name$eq': ''
    }

    data = do_api_with_openapi(method='GET',
                               uri=uri,
                               access_key=ACCESS_KEY,
                               secret_key=SECRET_KEY,
                               data=params)

    records = data.get('data',{}).get('list',[])
    return records
