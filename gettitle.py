import urllib,requests
import re
import json
import _thread
import dns.resolver
import Dictionaries
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
  page = requests.get(url,headers={"User-Agent":'InfoScanner powerby Master_Perng'})
  title = re.findall('<title>(.+)</title>',page.text)
  ICP = re.findall('(ICP备.+号)',page.text)[0:]
  PoliceNo = re.findall('(公网安备.+号,page.text)',page.text)
  page.encoding = 'utf-8'
  return title,ICP,PoliceNo
 except Exception:
  print('ERROR')
 #print(page.text)

if __name__ == '__main__':
 url = input()
 print(getHttpInfo(url))
