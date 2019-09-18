# coding=utf-8
import re
from aip import AipSpeech
class BaiDuAPI:
    def __init__(self,path):
        self.APP_ID = '10885740'
        self.API_KEY = 'tGchZ1dM8FpmjIIfMOFlqqkn'
        self.SECRET_KEY = 'zCmvmmWrwol0nh6UcvWPG3PXLmnavBGc'
        self.aipSpeech = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.filePath=path
        #print(self.filePath)
# 定义常量
    def get_file_content(self):
        with open(self.filePath, 'rb') as fp:
            return fp.read()

# 初始化AipSpeech对象
    def out_words(self):
        return self.aipSpeech.asr(self.get_file_content() ,'wav', 16000, {
    'lan': 'zh',
}).get('result')[0]
# 读取文件
if __name__=="__main__":
    BaiDuAPI(r'd:\pydate\voice.wav').out_words()
# 识别本地文件

