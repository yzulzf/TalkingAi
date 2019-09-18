# coding=utf-8
import requests
import json
class TulingRebot:
    def __init__(self,words):
        self.key='a8a0f074197d4ab5a67dac988240fbbc'
        self.info=words
        self.url='http://www.tuling123.com/openapi/api?key='+self.key+'&info='+self.info
        self.res = requests.get(self.url)
        self.res.encoding="utf-8"
        self.jd = json.loads(self.res.text)
    def getInfo(self):
        return self.jd['text']


if __name__=="__main__":
    print(TulingRebot('今天星期几').getInfo())