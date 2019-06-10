#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  time
import  json
import requests

import random

# class test_str:
#     def __init__(self):
#         self.text = ''

def GetZhouGong(msg):
    name=msg.text[2:]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    url = 'http://v.juhe.cn/dream/query?q='+name+'&key=cid=&full=&key=XXXXXXXXXXXXXXX' #周公解梦接口
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data =data['result']
    print(data)
    try:
        zg = '解梦结果:' + '\n' + '发送时间:' + NTime + '\n'
        for i,item in enumerate(data):
            zg += str(i+1) + '.梦到：' + item['title'] + '\n' \
            + '结果：' + item['des'] + '\n'
        msg.reply(zg)
    except BaseException:
        msg.reply( '小女子无法解答公子的梦境~')


# test_str = test_str()
# test_str.text = '丢黄金'
# res = GetZhouGong(test_str)


