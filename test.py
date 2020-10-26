import getDNS
import getWeb
class target():   #目标基类
    url = ''              #URL
    domain = ''           #域名
    port = ['']           #端口列表
    IP = ''               #IP
    title = ''        # title
    ICP = ''          # ICP备案号
    gaID = ''         # 公安备案号
    CMS = ''          # CMS 版本
    lang = ''         # 后台语言
    ResponseCode = '' # 响应码
    Server = ''       # 服务器类型
    CDN = ''
#    def getWebInfo(self):


    def getDomain(self):
        getDNS.URL_Refine(self.url)
    def getIP(self):
        getDNS.get(self.url)
    #def getPort(self):
        #


if __name__ == '__main__':
    zf = target()
    zf.url = 'http://www.perng.cn'
    print(zf.getDomain())
    zf.getIP()