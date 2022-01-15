from cutesdk.wxapp import ACCESS_TOKEN

import utils as test_utils

sdk = test_utils.get_sdk()

api_path = '/wxa/getnearbypoilist'
params = {
    'access_token': ACCESS_TOKEN,
    'page': 1,
    'page_rows': 10,
}

res = sdk.api_get(api_path, params)

print(res)
