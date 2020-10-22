import urllib,requests
import re
import json
import _thread
import dns.resolver

#while(url) :
def getHttpInfo (url):                 #Web信息分析   title抓取
 try:
  page = requests.get(url,headers={"User-Agent":"InfoScan Master_Perng"})
  title = re.findall('<title>(.+)</title>',page.text)
  ICP = re.findall('(ICP备.+号)',page.text)[0:]
  page.encoding = 'utf-8'
  print(title,ICP,page.status_code)
 except Exception:
  print('ERROR')
 #print(page.text)

if __name__ == '__main__':
 url = input()
 getHttpInfo(url)
