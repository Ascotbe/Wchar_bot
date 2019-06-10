#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  time
import  json
import requests

import random

def del_zero(time):#因为接口有的不识别2019-03-04这种类型只识别2019-3-4这种类型所以把数据修改
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
    res = y+'-'+m+'-'+d
    return res


def GetWanNianLi(msg):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTime = del_zero(nowTime)
    url = 'http://v.juhe.cn/calendar/day?date='+nowTime+'&key=XXXXXXXXXXXXXXX' #万年历接口
    Huangli='http://v.juhe.cn/laohuangli/d?date='+nowTime+'&key=XXXXXXXXXXXXXXX'#黄历接口
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    repS = requests.get(Huangli, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data =data['result']
    data =data['data']
    dataS = json.loads(repS.text)
    dataS=dataS['result']

    starhtml = '今日黄历：'+'\n'\
    + '          发送时间:'+ NTime+ '\n'\
    + '          今天是：' + data['weekday'] + '\n'\
    + '          今年生肖：' + data['animalsYear'] + '\n'\
    + '          纪年：' + data['lunarYear'] + '\n'\
    + '          农历：' + data['lunar'] + '\n'\
    + '          五行：' + dataS['wuxing'] + '\n'\
    + '          冲煞：' + dataS['chongsha'] + '\n'\
    + '          彭祖百忌：' + dataS['baiji'] + '\n'\
    + '          吉神宜趋：' + dataS['jishen'] + '\n'\
    + '          凶神宜忌：' + dataS['xiongshen'] + '\n'\
    + '          宜：' + data['suit'] + '\n'\
    + '          忌：' + data['avoid'] + '\n'
    msg.reply(starhtml)
