# coding=utf-8
from Day1.语音交互.语音输入 import recoder
from Day1.语音交互.Tulingclass import TulingRebot
from Day1.语音交互.提取语音文字类 import BaiDuAPI
from Day1.语音交互.语音合成类 import YuyinGet
#import os
import pygame
import time
r=recoder()
r.recoder()
r.savewav(r"d:\pydate\input.wav")
baidu=BaiDuAPI(r"d:\pydate\input.wav")
mywords=baidu.out_words()
print(type(mywords))
tu=TulingRebot(mywords)
response=tu.getInfo()
res=YuyinGet(response)
res.writeFile()
file=r'd:\pydate\success.mp3'
pygame.mixer.init()
print("回答ing")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(6)
pygame.mixer.music.stop()