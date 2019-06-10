#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  time
import  json
import requests

import random


def del_zero(time):#因为接口有的不识别2019-03-04这种类型只能识别3/5这种类型的
    block = time.split('-')
    y =  block[0]
    m, d = block[1:3]
    if (len(m) == 2):
        if m[0] == '0':
            m = m.replace('0', '')
            # print(m)
    if (len(d) == 2):
        if d[0] == '0':
            d = d.replace('0', '')
            # print(d)
    res = m+'/'+d
    return res


def GetLiShi(msg,all = False):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTime = del_zero(nowTime)
    url = 'http://v.juhe.cn/todayOnhistory/queryEvent.php?date='+nowTime+'&key=XXXXXXXXXXXXXXX' #万年历接口
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data =data['result']

    starhtml = '历史上的今天：' + '\n' \
    + '当前发送时间:' + NTime + '\n'
    for i,item in enumerate(data):
        if all == False:
            if (i <= 9):
                starhtml += item['date'] + '\n'\
                + item['title'] + '\n'
        else:
            starhtml += item['date'] + '\n' \
            + item['title'] + '\n'

    msg.reply(starhtml)
