# -*- coding:utf-8 -*-
import getWeb
import getDNS
import readfile
import fire
def logo():
  print("""
  
ooo        ooooo                        .                      
`88.       .888'                      .o8                      
 888b     d'888   .oooo.    .oooo.o .o888oo  .ooooo.  oooo d8b 
 8 Y88. .P  888  `P  )88b  d88(  "8   888   d88' `88b `888""8P 
 8  `888'   888   .oP"888  `"Y88b.    888   888ooo888  888     
 8    Y     888  d8(  888  o.  )88b   888 . 888    .o  888     
o8o        o888o `Y888""8o 8""888P'   "888" `Y8bod8P' d888b        
                                              
ooooooooo.   oooooooooooo ooooooooo.   ooooo      ooo   .oooooo.    
`888   `Y88. `888'     `8 `888   `Y88. `888b.     `8'  d8P'  `Y8b   
 888   .d88'  888          888   .d88'  8 `88b.    8  888           
 888ooo88P'   888oooo8     888ooo88P'   8   `88b.  8  888           
 888          888    "     888`88b.     8     `88b.8  888     ooooo 
 888          888       o  888  `88b.   8       `888  `88.    .88'  
o888o        o888ooooood8 o888o  o888o o8o        `8   `Y8bood8P'  
  """)

if __name__=='__main__' :
  logo()
  url_File=input()
  url=readfile.ReadTxtName(url_File)
  for url_ in url:
    getWeb.getHttpInfo(url_)
    getDNS.get(url_)




'''  class target():   #目标基类
    url = ''              #URL
    domain = ''           #域名
    ICP = ''              #ICP备案号
    PoliceNo = ''         #公安备案号
    port = ['']
    IP = ''
    def get'''




