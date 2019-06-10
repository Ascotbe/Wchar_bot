 # 有道翻译结果获取
 
from urllib import request, parse
import json
 
def FanYiHS(msg):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = msg.text[2:]  # 要翻译的内容可以更改
    Form_Date['doctype'] = 'json'


    data = parse.urlencode(Form_Date).encode('utf-8') #数据转换
    response = request.urlopen(req_url, data) #提交数据并解析
    html = response.read().decode('utf-8')  #服务器返回结果读取
    #print(html)
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  #以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    msg.reply(translate_results)
    #print(translate_results) #输出结果




