#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

import  json

import random
def GetXingZuo(msg):
    name=msg.text[4:]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    url = 'http://web.juhe.cn:8080/constellation/getAll?consName='+str(name)+'&type=today&key=XXXXXXXXXXXXXXX'
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    starhtml = '今日'+str(name)+'运势：'+ '\n'\
        + '          综合指数：' + data['all'] + '\n'\
        + '          幸运色：' + data['color'] + '\n'\
        + '          健康指数：' + data['health'] + '\n'\
        + '          爱情指数：' + data['love'] + '\n'\
        + '          财运指数：' + data['money'] + '\n'\
        + '          速配星座：' + data['QFriend'] + '\n'\
        + '          工作指数：' + data['work'] + '\n'\
        + '          今日概述：' + data['summary'] + '\n'\

    msg.reply(starhtml)
