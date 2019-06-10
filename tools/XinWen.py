#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from requests import exceptions
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from threading import Timer
import re
import  time
import http
import  json
import datetime
import random

def GetXinWen(msg, all = False):
    type=msg.text[:4]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    url = 'http://v.juhe.cn/toutiao/index?type='+str(type)+'&key=XXXXXXXXXXXXXXX'
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    data = json.loads(rep.text)
    data = data['result']
    data = data['data']
    item = []
    obj = {}
    html = '今日'+str(type)+'：'+ '\n'
    for xh, i in enumerate(data):
        if all == False:
            if (xh <= 4):
                html = html + '标题：' + i['title'] + '\n'\
                        + '链接：' + i['url'] + '\n'\
                        + '分类：' + i['category'] + '\n'\
                        + '来自：' + i['author_name'] + '\n'\
                        + '时间：' + i['date'] + '\n'\
                        + '-----------------------------------------------' + '\n' +'\n'
        else:
            html = html + '标题：' + i['title'] + '\n' \
                   + '链接：' + i['url'] + '\n' \
                   + '分类：' + i['category'] + '\n' \
                   + '来自：' + i['author_name'] + '\n' \
                   + '时间：' + i['date'] + '\n' \
                   + '-----------------------------------------------' + '\n' + '\n'


    msg.reply(html)
