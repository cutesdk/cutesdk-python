import utils as test_utils

sdk = test_utils.get_sdk()

code = '071VWk0w3TcmOX2LFQ2w3kW1Oq4VWk0m'

res = sdk.code2session(code)

print(res)
