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


#axis:轴的位置 startstr:起始字符串 data:数据
axis = 20
startstr = " "*(axis-5)+"---start2019:\n"+ " "*axis+"|"
endstr =" "*(axis-4)+":2019end---"


#data = [{'time':'06/32','something':'hhhhh'},\
#        {'time':'02/14','something':'ok'}]


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
    return str1,str2,str3

def printTimeline():
    '''
        打印时间轴
    '''
    print(startstr)
    data = readData()
    for item in data:
        print(*createNode(item['time'],item['something']),sep='\n')
    print(endstr)


def readData():
    data = []
    startflag = 0
    with open('./timeline.py') as f:
        for line in f:
            if line.startswith("#data_start"):
                startflag = 1
                continue
            if line.startswith("#data_end"):
                break
            if startflag:
                if line[-1] == '\n':
                    line = line[:-1]
                if line[-1] == '\r':
                    line = line[:-1]
                data.append({'time':line[1:6],'something':line[6:]})
    return data

def writeData(t,sth):
    lineStr = "#"+t+sth+' '*8 +'\n'
    lineEnd = "#data_end"
    with open("./timeline.py",'r+b') as f:
        for line in f:
            if line.startswith("#data_end".encode('utf-8')):
                backstep = -len(line) 
                f.seek(backstep,1)
                f.write(lineStr.encode('utf-8'))
                f.write(lineEnd.encode('utf-8'))
                break
    printTimeline()
                

    

printTimeline()


#data_start
#04/21linux开发环境搭建
#04/22时间轴脚本                
#data_end
