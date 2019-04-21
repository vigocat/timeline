# -*- coding: utf-8 -*-
'''
autor: vigocat   2019/04/21 23:45
description: timeline
notes: python3

print("              ---start2019:")
print("                   |")
print("         04/02-----|")
print("                   o-------- linux工作环境搞定 00:10")
print("                   |")
print("           05/23---|")
print("                   o----- linux工作环 00:10")
print("                   |")
print("               :2019end---")

'''
import random


#axis:轴的位置 startstr:起始字符串
axis = 20
startstr = " "*(axis-5)+"---start2019:\n"+ " "*axis+"|"
endstr =" "*(axis-4)+":2019end---"


def createNode(t,sth):
    '''
       添加一个节点
       参数:t 时间 sth事件
    '''
    r1 =  random.randint(3,7)
    r2 =  random.randint(4,15)
    str1 = " "*(axis-5-r1)+t+'-'*r1+'|'
    str2 = " "*axis+"o"+"-"*r2+" "+sth
    str3 = " "*axis+"|"
    return [str1,str2,str3]

def printTimeline():
    '''
       打印时间轴
    '''
    print(startstr)
    print(*createNode("06/32","hhhhh"),sep = "\n")
    print(*createNode("02/14","成功了哈哈哈"),sep = "\n")
    print(endstr)
    
printTimeline()

