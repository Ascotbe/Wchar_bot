#!/usr/bin/python env
# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_nba(msg):
    resp = urlopen('https://m.hupu.com/nba/game')
    soup = BeautifulSoup(resp, 'html.parser')
    tagToday = soup.find('section', class_="match-today")
    nbaHtml = '今日NBA比赛结果：' + '\n' + '\n'
    for tag in tagToday.find_all('a', class_='match-wrap'):
        nbaHtml = nbaHtml + tag.find('div', class_='away-team').span.get_text() + '    ' + tag.find('strong',
                                                                                                    class_='').span.get_text() + '    ' + tag.find(
            'div', class_='home-team').span.get_text() + '  (' + tag.find('div',
                                                                          class_='match-status-txt').get_text() + ')' + '\n'

    msg.reply(nbaHtml)


