# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:53:04 2020

@author: tyj
"""
import pygame
def make_voice(x):
    pygame.mixer.init()
    voi = chinese_to_pinyin(x).split()
    for i in voi:
        if i == 'XXXX':  #处理'XXXX'的音，可将其忽略
            continue
        pygame.mixer.music.load(i + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    return None


def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_py.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += 'XXXX ' #非法字符我们用XXXX代替
    print(y)
    return y

if __name__=='__main__':
    print("hello")
    while True:
        p=input("请输入文字：")
        make_voice(p)
