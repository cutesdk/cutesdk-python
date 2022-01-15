# -*- coding: utf-8 -*-
'''
小程序请求 GET 类型接口测试
'''

import utils as test_utils

sdk = test_utils.get_sdk()

code = 'xxx'

res = sdk.code2session(code)

print(res)
