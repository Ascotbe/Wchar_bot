#!/usr/bin/python env
# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re
import requests
import random
import datetime
import  time

def GetWeather(msg):
    city=msg.text[4:]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    url = 'https://free-api.heweather.com/s6/weather/now?location='+city+'&key=XXXXXXXXXXXXXXX'
    PMurl = 'https://free-api.heweather.com/s6/air/now?parameters&location='+city+'&key=XXXXXXXXXXXXXXX'
    # 设定超时时间，防止被网站认为是爬虫
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    pm = requests.get(PMurl, headers=header, timeout=timeout)

    result = ''
    temp = rep.json()
    temp = temp['HeWeather6'][0]
    update = temp['update']
    now = temp['now']
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pm = pm.json()
    pm = pm['HeWeather6'][0]

    print(now)

#区分县级市和市  免费接口没办法查到县级市的天气

    if pm['status'] == 'permission denied':
        # 县级市
        resulta = city + '实时天气预报-' + '\n'+ '更新时间：' + update['loc'] + '\n'+ '          当前天气：' + now['cond_txt'] + '\n'+ '          当前温度：' + now['tmp'] + '°C' + '\n'+ '          体感温度：' + now['fl'] + '°C' + '\n'+ '          风向：' + now['wind_dir'] + ' ' + now['wind_sc'] + '级 ' + now['wind_spd'] + '公里/小时' + '\n'+ '          相对湿度：' + now['hum'] + '%' + '\n'+ '          降水量：' + now['pcpn'] + 'ml' + '\n' + '          能见度：' + now['vis'] + '公里' + '\n'+ '          云量：' + now['cloud'] + '\n'
        result = resulta + '发送时间：' + nowTime + '\n'
    else:        # 非县级市
        airnow = pm['air_now_city']
        result = city +  '实时天气预报-' + '\n'\
        + '更新时间：'+ update['loc'] + '\n'\
        + '          当前天气：'+ now['cond_txt'] + '\n'\
        + '          当前温度：'+ now['tmp'] + '°C' + '\n'\
        + '          体感温度：'+ now['fl'] + '°C' + '\n'\
        + '          风向：'+ now['wind_dir'] + ' ' + now['wind_sc'] + '级 '+ now['wind_spd'] + '公里/小时'+ '\n'\
        + '          相对湿度：'+ now['hum'] + '%' + '\n'\
        + '          降水量：'+ now['pcpn'] + 'ml' + '\n'\
        + '          能见度：'+ now['vis'] + '公里' + '\n'\
        + '          云量：'+ now['cloud']  + '\n'\
        + '-----------------------------------' + '\n'\
        + '当前空气质量：'+'\n'\
        + '          空气质量指数：'+ airnow['aqi']+'\n'\
        + '          主要污染物：'+ airnow['main']+'\n'\
        + '          空气质量：'+ airnow['qlty']+'\n'\
        + '          二氧化氮指数：'+ airnow['no2']+'\n'\
        + '          二氧化硫指数：'+ airnow['so2']+'\n'\
        + '          一氧化碳指数：'+ airnow['co']+'\n'\
        + '          pm10指数：'+ airnow['pm10']+'\n'\
        + '          pm25指数：'+ airnow['pm25']+'\n'\
        + '          臭氧指数：'+ airnow['o3']+'\n'

        result =  result + '发送时间：' +  nowTime + '\n'

    msg.reply(result)