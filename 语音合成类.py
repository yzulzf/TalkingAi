# coding=utf-8
from aip import AipSpeech
class YuyinGet:
    def __init__(self,words):
        self.APP_ID = '10890994'
        self.API_KEY = '5g5DnvijgwEA1OIkwR7UUpLp'
        self.SECRET_KEY = 'strGCz8L4GyVItWbvz1frxeV2KaiLehp '
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.result = self.client.synthesis(words, 'zh', 1, {
            'vol': 5,'per':1
        })

    def writeFile(self):
        if not isinstance(self.result, dict):
            with open(r'd:\pydate\success.mp3', 'wb') as f:
                f.write(self.result)

if __name__=="__main__":
    YuyinGet("你真棒！我的宝贝").writeFile()