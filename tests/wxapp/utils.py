from cutesdk.wxapp import WxApp


def get_sdk():
    appid = 'wx25da2eca8fa3f4ef'
    app_secret = '1324f564b26f9f8006515e13660876ef'

    sdk = WxApp(appid, app_secret)

    return sdk
