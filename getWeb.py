#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,requests
import re
import json
import _thread
import Dictionaries
import random


#while(url) :
def getHttpInfo (url):                 #Web信息分析   title抓取
 """try:
  x=Dictionaries.UserAgent
  if bool(x) == 0:"""
 # x = 'InfoScanner powerby Master_Perng'
 """ page = ''
 title = ''
 ICP = ''
 PoliceNo = ''  """
 try:
   UserAgentKey = random.sample(Dictionaries.UserAgent.keys(), 1)
   user_agent = Dictionaries.UserAgent[UserAgentKey[0]]
   page = requests.get(url,headers={"User-Agent":user_agent},timeout=1)  #0.5秒未建立连接则视为超时
   page.encoding = 'utf-8'
   title = re.findall('<TITLE>(.+)</TITLE>',page.text,re.IGNORECASE)  #正则匹配大小写不敏感
   ICP = re.findall('(ICP备.+号)',page.text)[0:]
   PoliceNo = re.findall('(公网安备 .+号,page.text)',page.text)
   page.encoding = 'utf-8'
   print(url,title,ICP,PoliceNo,page.status_code)    #目前输出，可改为return
   return  0
 except Exception:
   print(url,'TimeOut')
 #print(page.text)

if __name__ == '__main__':
 url = input()
 print(getHttpInfo(url))
