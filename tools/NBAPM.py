#!/usr/bin/python env
# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_rank(msg):
    resp = urlopen('https://m.hupu.com/nba/stats')
    soup = BeautifulSoup(resp, 'html.parser')
    east = soup.find_all('li', class_="weast")[0]
    west = soup.find_all('li', class_="weast")[1]
    rankHtml = '今日NBA东部排名：（1.排名  2.球队  3.胜负  4.胜负差  5.最近情况）' + '\n' + '\n'
    for tag in east.find_all('li', class_=''):
        list = tag.find('p', class_='right-data')
        rankHtml = rankHtml + tag.find('span', class_='rank').get_text() + '. ' + tag.find('div',
                                                                                           class_='').h1.get_text() + '    ' + \
                   list.find_all('span')[0].get_text() + '    ' + list.find_all('span')[1].get_text() + '    ' + \
                   list.find_all('span')[2].get_text() + '\n'

    rankHtml = rankHtml + '\n' + '\n' + '---------------------------------------------' + '\n' + '\n'
    rankHtml = rankHtml + '今日NBA西部排名：（1.排名  2.球队  3.胜负  4.胜负差  5.最近情况）' + '\n' + '\n'
    for tag in west.find_all('li', class_=''):
        list = tag.find('p', class_='right-data')
        rankHtml = rankHtml + tag.find('span', class_='rank').get_text() + '. ' + tag.find('div',
                                                                                           class_='').h1.get_text() + '    ' + \
                   list.find_all('span')[0].get_text() + '    ' + list.find_all('span')[1].get_text() + '    ' + \
                   list.find_all('span')[2].get_text() + '\n'

    msg.reply(rankHtml)