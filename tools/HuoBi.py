#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  time
import  json
import requests

import random

def GetHuoBi(msg):
    name=msg.text[2:]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    c1, c2 = s2s(name)
    if c1=='not found' or c2=='not found':#如果一个币种没找到的话就返回
        msg.reply('公子请检查是否输入正确~')



    url = 'http://op.juhe.cn/onebox/exchange/currency?key=XXXXXXXXXXXXXXX&from='+c1+'&to='+c2
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    NTime = datetime.datetime.now().strftime('%Y-%m-%d')
    if data['reason']=='查询成功!'or data['reason']=='successed':
        data=data['result']
        HB='查询时间:'+NTime+'\n'
        for i in data:
            HB+=i['currencyFD']+i['currencyF_Name']+'='+i['result']+i['currencyT_Name']+'\n'
        HA=HB+'汇率更新于'+i['updateTime']
        msg.reply(HA)
    else:
        msg.reply('小女子无法识别公子输入的币种')

def load(path = 'tools/huobi.json'):#打开JSON   ！！！！注意！！！JSON的文件要于主调用的PY文件同级不然会找不到还不报错
    with open(path) as json_file:
        data = json.load(json_file)
        return data

t = load()
def s2s(text):#分割带有转的文本然后遍历找到与JSON中相对于的文字最后提取出文字同级的内容
    sp = text.split('转')
    c1 = c2 = ''
    res = t['result']['list']
    for item in res:
        if item['name'] == sp[0]:
            c1 = item['code']
        if item['name'] == sp[1]:
            c2 = item['code']
    if c1 == '' or c2 == '':
        return 'not found',  'not found'
    return c1, c2




# s2s('汇率人民币转美元')


# GetHuoBi('汇率新加坡元转人民币')


# c1, c2 = s2s('sb元转美元')

# print(c1,'to',c2)