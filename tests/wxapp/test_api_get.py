# -*- coding: utf-8 -*-
'''
小程序请求 GET 类型接口测试
'''

from cutesdk import wxapp
import utils as test_utils

sdk = test_utils.get_sdk()

api_path = '/wxa/getpaidunionid'
params = {
    'access_token': wxapp.ACCESS_TOKEN,
    'openid': 'oLW495c2KVrduEpiSGDpHp7qKqCc',
}

res = sdk.api_get(api_path, params)

print(res)
