# coding=utf-8
import requests
import json

key='a8a0f074197d4ab5a67dac988240fbbc'
while True:#//主循环
    info = input('\n我：')#//输入对话信息
    url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info#//组成url
    res = requests.get(url)#//得到网页HTML代码
    res.encoding = 'utf-8'#//防止中文乱码
    jd = json.loads(res.text)#/将得到的json格式的信息转换为Python的字典格式
    print('\nTuling: '+jd['text'])#//输出结果