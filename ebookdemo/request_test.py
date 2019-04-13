# -*- coding: utf-8 -*-
import requests
from PIL import Image

if __name__ == '__main__':
    # url = "http://pp.myapp.com/ma_icon/0/icon_52455981_1554954481/256"
    url = 'http://fastcfg.suning.com/maa/getConfigByVerAll.do'
    # url='http://apm.suning.cn/customSDK.gif'
    AppKey = '46076815e9b449f79be9f6582137796b'
    Version = 'v1.0'

    headers = {
        'Connection': "keep-alive",
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; PIC-AL00 Build/HUAWEIPIC-AL00)",
        'Accept-Encoding': "gzip",
        'Cookie': 'tradeMA=78; authId=si505472A406CF197D74CA6D944B8C5AD9; custno=7038268238'
    }

    data = '[{"Version":"v1.0","AppKey":"46076815e9b449f79be9f6582137796b"}]'
    # data='sys_data=29fde88202134aaa9513d5cd77872c96%7C7.6.2%7C%E6%89%8B%E6%9C%BA%7CHUAWEI%7C8.0.0%7CHUAWEIPIC-AL00%7C864274037245699%7C192.168.100.118%7C%E5%B9%BF%E4%B8%9C%7C%E6%B7%B1%E5%9C%B3%E5%B8%82%7CWIFI%7C%E5%85%B6%E4%BB%96%7C%7C11006%7CC3.5.0.6%7C1%7C1080x1920%7C%E8%8B%8F%E5%AE%81%E6%98%93%E8%B4%AD%7C269%7Ccom.suning.mobile.ebuy%7CPIC-AL00+8.0.0.360%28C00%29%7C0%7C26%7C%7C%7C%7C%7C%7C%7C1&custom_data=20190413141928047%7CIPCC%7C%7CSNmobile4%7Cemodule%3A%E6%96%B0%E9%A1%B5%E9%9D%A2%E8%B7%AF%E7%94%B1%3AS%23%24%23eif%3A%3AS%23%24%23estatus%3A1%3AS%23%24%23eerrcode%3A%3AS%23%24%23erouterip%3A%3AS%23%24%23eerrdetail%3A%3AS%23%24%23ecost%3A0%3AD&sign=1b6382049b9822329b74894e76ae0626'

    response = requests.request("Post", url, data=data,
                                headers=headers)

    if 'image' in response.headers.get('Content-Type'):
        # data = response.content
        # img = Image.open(data)
        # img.show()
        pass
    if ('text' in response.headers.get('Content-Type')) | ('json' in response.headers.get('Content-Type')):
        print(response.text)
