from cutesdk.wxapp import ACCESS_TOKEN

import utils as test_utils

sdk = test_utils.get_sdk()

api_path = '/datacube/getweanalysisappiddailyretaininfo'
params = {
    'access_token': ACCESS_TOKEN,
}
data = {
    'begin_date': '20220102',
    'end_date': '20220102',
}

res = sdk.api_post(api_path, params, data)

print(res)
