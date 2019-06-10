#!/usr/bin/python env
# -*- coding:utf-8 -*-
#导入包
import datetime
from hyperlpr import *
import numpy as np
#导入OpenCV库
import cv2
from PIL import Image, ImageDraw, ImageFont
#读入图片

casc = 'models/haarcascade_frontalface_alt.xml'
classifier = cv2.CascadeClassifier(casc)

NTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def getLPR(path):
    image = cv2.imread(path)

    #识别结果
    res = HyperLPR_PlateRecogntion(image)

    font = ImageFont.truetype('models/NotoSansCJKjp-Black.otf', 20)
    lpr_str = '检测时间:'+NTime+'\n' \
              '检测到的车牌号为:' + '\n'
    for item in res:#图片绘图
        lpr = item[0]
        pre = item[1]
        bbox = item[2]
        [x1, y1, x2, y2] = bbox
        cv2.rectangle(image, (x1, y1),(x2, y2), (0, 0, 255), 2)
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#cv2.COLOR_BGR2RGB因为OPENCV的RGB同道是倒着来的所有闲用工具把BGR转成正常的RGB
        draw = ImageDraw.Draw(img_PIL)
        draw.text((x1,y1-25), lpr, font=font, fill=(255,0,0))#画框
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)#吧画好的RGB类型转成BGR
        lpr_str +=lpr+'\n'#输出车牌号

    cv2.imwrite('lpr.jpg', image)#写入图片

    return len(res), lpr_str


def getFaces(path):
    image = cv2.imread(path)
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(
        gary,
        scaleFactor=1.1,
        minNeighbors=2
    )
    for x, y, w, h in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)#行车XY的宽度个高转换

    cv2.imwrite('face.jpg', image)
    return len(faces)

