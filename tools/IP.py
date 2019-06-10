#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  time
import  json
import requests

import random

def GetIP(msg):
    IP=msg.text[4:]
    print(IP)
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    url = 'http://apis.juhe.cn/ip/ipNew?ip='+IP+'&key=XXXXXXXXXXXXXXX' #IP查询接口
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    judge=data['resultcode']
    if judge=='200':#判断查询是否成功
        data =data['result']
        print(data)
        if data['Province']!=''and data['City']!='' and data['Isp']!='':#判断全都不为空时
            IPname='查询时间:'+NTime+'\n'\
            +'国家:'+data['Country']+'\n' \
            +'省份:'+data['Province']+'\n'\
            +'县市(区):'+data['City']+'\n'\
            +'运营商:'+data['Isp']
            msg.reply(IPname)
        elif data['Province']!=''and data['City']!=''and data['Isp']=='':#判断运营商为空时
            IPname='查询时间:'+NTime+'\n'\
            +'国家:'+data['Country']+'\n' \
            +'省份:'+data['Province']+'\n'\
            +'县市(区):'+data['City']+'\n'
            msg.reply(IPname)
        elif data['Province']!=''and data['City']=='':#判断县市为空时
            IPname='查询时间:'+NTime+'\n'\
            +'国家:'+data['Country']+'\n' \
            +'省份:'+data['Province']+'\n'
            msg.reply(IPname)
        else:#只能查到国家时
            IPname = '查询时间:' + NTime + '\n' \
            +'小女子只查询到该IP的国家' + '\n'\
            + '国家:' + data['Country']
            msg.reply(IPname)
    else:#输入错误时
        msg.reply('小女子无法查到公子输入的IP')




