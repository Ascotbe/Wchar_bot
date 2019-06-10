#!/usr/bin/python env
# -*- coding:utf-8 -*-
from wxpy import *
from tools.tianqi import *
import os
from tools.NBAPM import *
from tools.ss_pythonic_spider import *
from tools.NBA import *
from tools.FanYi import *
from tools.XingZuo import *
from tools.XinWen import *
from tools.manager import *
from tools.WanNianLi import *
from tools.LiShi import *
from tools.ZhouGong import *
from tools.IP import *
from tools.HuoBi import *
from tools.scan import *
from tools.TuiSong import *
import datetime

from models.ImageScan import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path = True)
bot.enable_puid()
manager = manager()#创建CLass类

NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#帮助文档有待完善
bangzhu="""

1.在线基情聊天（关闭了骂人功能)
    exa:@me 内容
2.帮助文档
    exa:@me -help or -h
3.ssr帐号
    exa:@me 账号 or @me 全部账号（目前功能已下线)
4.ssr下载
    exa:@me SSR/ssr
5.笑话
    exa:@me 笑话
6.翻译(可以翻译中文和英文)
    exa:翻译 i am baby
7.端口扫描
    exa:scan 192.168.1.1
8.天气查询 城市
    exa:天气查询 北京
9.星座查询
    exa:星座查询 白羊座
10.今日NBA球队排名
    exa:@me 球队排名
11.今日NBA比赛结果
    exa:@me NBA
12.今日新闻
    exa:头条新闻
        社会新闻
        娱乐新闻
        体育新闻
        (默认输出5条需要全部输出请加-a)
13.今日黄历
    exa:今日黄历 
14.历史上的今天
    exa:历史上的今天 or 历史上的今天-a(输出全部,默认输出前面10条) 
15.周公解梦
    exa:解梦XX(XX为你的梦境)  
16.IP查询
    exa:IP查询 192.168.1.1 
17.汇率转换
    exa:汇率 XX转XX(XX为 币种)            
18.人脸扫描
    exa:直接发图就行(如果管理员关闭则无法运行)
19.车牌识别
    exa:和人脸扫描一样
"""

SSR_DiZi=""" 
/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心
1. Windows客户端：https://github.com/shadowsocksrr/shadowsocksr-csharp/releases                            
2. Mac客户端：https://github.com/flyzy2005/ss-ssr-clients/raw/master/ssr/SS-X-R.zip                        
3. Linux客户端：https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation                           
4. Android/安卓客户：https://github.com/flyzy2005/ss-ssr-clients/raw/master/ssr/ShadowsocksR-3.4.0.8.apk
/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心
"""



# SSR列表
def ssr_work(file_name):
    ssr_list = []
    with open(file_name, 'r') as f:
        for i in f.readlines():
            ssr_list.append(i)
    return ssr_list
#笑话列表
def Xiao_work(file_name):#转换成列表
    XiaoHua_list = []
    with open(file_name, 'r') as f:
        for i in f.readlines():
            XiaoHua_list.append(i)
    return XiaoHua_list



#图灵APIkey
tuling = Tuling(api_key='XXXXXXXXXXXXXXX')



def TuiSong(time1):#调用推送函数并且传入特定的值，让机器人推送不同的人
    if time1=='1':
        friend = bot.friends().search(u'主人')[0]
        #print(friend)
        N=GetTuiSong(msg='1')
        friend.send(N)
    elif time1 == '2':
        friend = bot.friends().search(u'母后')[0]
        #print(friend)
        N = GetTuiSong(msg='2')
        friend.send(N)
    elif time1=='3':
        friend = bot.friends().search(u'父皇')[0]
        #print(friend)
        N=GetTuiSong(msg='3')
        friend.send(N)



@bot.register(Friend,TEXT)#处理好友文本消息
def print_others(msg):

    my_friends = bot.friends()  # 获取全部好友列表
    my_groups = bot.groups()  # 获取全部群信息
    if msg.text == manager.admin_key:#判断消息内容是否是存储的KEY如果是存为管理员
        unit = msg.chat
        manager.admin_id = unit.puid
        msg.reply('绑定管理员！')

    elif msg.chat.puid == manager.admin_id:

        if '地区' in msg.text:

            key=msg.text[2:]

            friends = my_friends.search(city=key)
            ID='查询时间:'+NTime+'\n'
            for xh, friend in enumerate(friends):
                ID+=str(xh+1)+'.'+ '网名:'+friend.nick_name+'\n'\
                    +'备注:'+friend.remark_name+'\n'\
                    +'省份:'+friend.province+'\n' \
                    +'城市:'+ friend.city + '\n' \
                    +'个性签名::'+ friend.signature + '\n'
            msg.reply(ID)  # 获取到好友的名称
        elif '网名' in msg.text:
            key = msg.text[2:]
            friends = my_friends.search(nick_name=key)
            ID='查询时间:'+NTime+'\n'
            for xh, friend in enumerate(friends):
                ID += str(xh + 1) + '.' + '网名:' + friend.nick_name + '\n' \
                      + '备注:' + friend.remark_name + '\n' \
                      + '省份:' + friend.province + '\n' \
                      + '城市:' + friend.city + '\n' \
                      + '个性签名::' + friend.signature + '\n'
            msg.reply(ID)  # 获取到好友的名称
        elif '群' in msg.text:
            msg.reply(my_groups)
        else:
            tuling.do_reply(msg)  #开启个人图灵机器人

    else:
        tuling.do_reply(msg)#开启个人图灵机器人
        #     key = msg.text[1:]
        #     print(key)
        #     groups = my_groups.search(keywords=key)
        #     group=groups.members
        #     print(my_groups)
        #     ID = '网名:' + groups.nick_name + '\n' \
        #           + '备注:' + groups.remark_name + '\n' \
        #           + '省份:' + groups.province + '\n' \
        #           + '城市:' + groups.city + '\n' \
        #           + '个性签名::' + groups.signature + '\n'
        #     print(ID)
        #     # i.province#用户所在省份
        #     # i.city#用户所在城市
        #     # i.nick_name#用户的原始名字
        #     # i.signature#用户的个性签名
        #     #i.alias#用户的微信号

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')
@bot.register(Group, TEXT)#处理群文本类型的数据
def group_msg(msg):

    if msg.is_at:

        """
            公共处理
        """
        if '-help' in msg.text or '-h' in msg.text:  # 第判断是否查看帮助文档
            msg.reply(bangzhu)
            #print(msg.reply)
        elif 'SSR'in msg.text  or 'ssr'in msg.text:  # 提供下载SSR地址
            msg.reply(SSR_DiZi)
        elif msg.text[:2]=='帐号':  # ssr帐号功能
            ssr_list = ssr_work("C:\\Users\\Ascotbe\\PycharmProjects\\untitled\\WXPY\\tools\\ss_ssr.txt")

            random.shuffle(ssr_list)  # 打乱列表顺序
            iRandom = ssr_list[0:1]  # 取出打乱数据的第一个值
            lib_d = " ".join(iRandom)  # 把列表转换成字符串
            msg.reply(lib_d)
        elif msg.text[:4]=='全部帐号':  # ssr全部帐号功能
            ssr_list = ssr_work("C:\\Users\\Ascotbe\\PycharmProjects\\untitled\\WXPY\\tools\\ss_ssr.txt")
            lib_d = " ".join(ssr_list)  # 把列表转换成字符串
            msg.reply(lib_d)
            #SSR账号的脚本好像有问题(待解决)
        elif '钓鱼岛' in msg.text or '台湾' in msg.text or '南海' in msg.text or '南沙群岛' in msg.text:  # 关键字过滤
            msg.reply('/爱心永远是中国的,我爱中国~/爱心')
        elif '习近平' in msg.text or '江泽民' in msg.text or '胡锦涛' in msg.text or '周恩来' in msg.text or '毛泽东' in msg.text or '邓小平' in msg.text or '刘少奇' in msg.text or '李先念' in msg.text or '杨尚昆' in msg.text or '李克强' in msg.text:  # 关键字过滤
            msg.reply('/爱心心系国家~/爱心')
        elif '中国' in msg.text or '共产党' in msg.text or '共青团' in msg.text or '中共' in msg.text:  # 关键字过滤
            msg.reply('/爱心我的心里只有党/爱心')
        elif 'NBA'in msg.text or 'nba'in msg.text:
            get_nba(msg)
        elif '球队排名'in msg.text:
            get_rank(msg)
        elif '更新文件'in msg.text:  # 更新一些爬取文件，以后爬取功能都可以放在这里
            Ssr_DinSiPaQu()  # SSR
            msg.reply( '陛下吩咐的事情已完成~')
        elif msg.is_at:
            txt = msg.text
            name = txt.split('@')[1] #如果账号改了名字就修改config.py文件下的LOCAL_NAME
            if name == manager.local_name:
                msg.reply('你他喵能不能看help？？？？') # 查看是不是捣乱
            else:
                tuling.do_reply(msg)

    elif msg.text[:4] == '天气查询':  # 天气查询
        #print(msg.text)
        GetWeather(msg)
    elif msg.text[:4] == '星座查询':# 查询星座今天的运势
        GetXingZuo(msg)

    elif msg.text[:4] =='头条新闻' or msg.text[:4] =='社会新闻' or msg.text[:4] =='娱乐新闻' or msg.text[:4] =='体育新闻':# 第三优先级查询今天新闻
        txt = msg.text
        if (txt.find('-a') != -1):#判断是否要输出全部新闻 如果不是只输出5条
            GetXinWen(msg, all=True)
        else:
            GetXinWen(msg)
    elif msg.text[:4]=='今日黄历':#查询具体的日子以及黄历
        GetWanNianLi(msg)
    elif msg.text[:6]=='历史上的今天':
        txt = msg.text
        if (txt.find('-a') != -1):  # 判断是否要输出历史信息，如果不是只输出10条
            GetLiShi(msg, all=True)
        else:
            GetLiShi(msg)
    elif msg.text[:2]=='解梦':#输入关键字查询具体的梦境
        GetZhouGong(msg)
    elif msg.text[:4]=='IP查询' or msg.text[:4]=='ip查询':#查询IP所在的地理位置
        GetIP(msg)
    elif msg.text[:2]=='汇率':#查询不通货币之间的实施汇率
        GetHuoBi(msg)
    elif msg.text[:2] == '翻译':  # 翻译功能
        print(msg.text[2:])
        FanYiHS(msg)
    elif msg.text[:4]=='scan' or msg.text[:4]=='Scan' or msg.text[:4]=='SCAN':#IP端口扫描
        GetScan(msg)


    elif msg.text[:3] == 'Ascotbe':
        msg.reply('他是你爸爸！！！！！')
    else:#设置好主人uin数字好关闭和开启机器人(好像会每天更新)
        unit = msg.member
        masterFlagFile_name = 'C:\\Users\\Ascotbe\\PycharmProjects\\untitled\\WXPY\\tools\\MasterFlag.txt'
        if unit.puid == manager.admin_id:
            print('处理管理员的消息！')
            if msg.text == '你好骚啊':
                msg.reply('你也是')
                '''!-------不反应或者反应-------!'''
            elif msg.text == '退下吧':  # 关闭人脸识别功能
                msg.reply('臣妾告退~')
                with open(masterFlagFile_name, 'w') as file_obj:
                    json.dump('0', file_obj)
                    print('已修改为0')
            elif msg.text == '爱妃':  # 开启人脸识别功能
                msg.reply('么么哒')
                with open(masterFlagFile_name, 'w') as file_obj:
                    json.dump('1', file_obj)
                    print('已修改为1')
        pass


@bot.register(Group,PICTURE)#处理图片类型参数
def face_msg(msg):
    f = open("C:\\Users\\Ascotbe\\PycharmProjects\\untitled\\WXPY\\tools\\MasterFlag.txt", "r")  # 设置打开原来设置的JSON文件
    masterFlag = json.load(f)#读取JSON文件

    #print(masterFlag)
    if masterFlag == '1':#当管理员开启人脸识别功能时进行人脸识别
                        #反之关闭这个功能
        image_name = msg.file_name
        msg.get_file('' + 'input.jpg')
        count, lpr_str = getLPR('input.jpg')
        facecout = getFaces('input.jpg')
        if count!=0:
            msg.reply_image("lpr.jpg")
            msg.reply(lpr_str)

        elif facecout!=0:
            msg.reply(u"检测到%d张人脸" % facecout)
            msg.reply_image("face.jpg")
        os.remove(image_name)


def main(h=5, m=00):#定时调用程序实现每日推送
    while True:
        now = datetime.datetime.now()
        if now.hour==h and now.minute==m:

            TuiSong(time1='1')
            time.sleep(5)
            TuiSong(time1='2')
            time.sleep(5)
            TuiSong(time1='3')
            time.sleep(55)




main()
embed()

