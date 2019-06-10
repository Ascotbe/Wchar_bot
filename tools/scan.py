#!/usr/bin/python env
# -*- coding:utf-8 -*-
import datetime
import  json
import requests

def GetScan(msg):
        s=msg.text[4:]
        header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'close'
            }

        NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        url = 'http://tools.hexlt.org/api/nmap'
        d = ({'target': s})#获取用户输入的IP存入POST中的JSON数据中
        r = requests.post(url, json=d)
        outcome=r.json()
        outcome=outcome['data']

        if outcome=='error IP address or host name only':#如果输入IP无法查询返回报错
                msg.reply('公子检查下输入的IP是否正确')
        else:
                scan = '查询时间:' + NTime + '\n' + outcome
                msg.reply(scan)


