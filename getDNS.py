import dns.resolver
import re
dns.resolver.default_resolver = dns.resolver.Resolver(configure = False) #初始化DNS配置
dns.resolver.default_resolver.nameservers = ['223.6.6.6','114.114.114.114','8.8.8.8'] #配置新的DNS服务器
# URL提取域名
def URL_Refine(URL) :
    # 正则匹配 /判断是否为url
    if bool(re.findall('/',URL))==False :
        return URL
    elif bool(re.findall('/',URL))==True :
        URL = URL+'/'
        domain = re.findall('://(.+)/',URL)
        return domain
#权威服务器查询
#def NS(URL) :

#别名查询
def CNAME(URL) :
     try:
      Record = dns.resolver.resolve(URL_Refine(URL)[0],'CNAME')    #URL_Refine去重后会返回list串，取第一个元素
      return Record
     except Exception:
      return A(URL)
#A记录查询
def A(URL) :
     try:
      Record = dns.resolver.resolve(URL_Refine(URL)[0],'A')
      return Record
     except Exception:
      return 0
#查询记录转换成字符串并输出
def Tran(Record) :
    try:
     for i in Record.response.answer:
      for j in i.items:
        print(j)
    except Exception:
        return 0
def get(URL):
    Tran(CNAME(URL))
if __name__=='__main__' :
    url=input()
    get(url)


# 10.20 CNAME函数在域名无CNAME参数时报错，打算先进行CNAME的布尔值进行判断，真发送给CNAME，假发送给A；
# 10.20 需要方法寻找权威DNS，并请求权威DNS获取信息