import requests
from bs4 import BeautifulSoup
import urllib
import re
import os
import time
import threading
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Host':'https://www.hanmanwo.net',
    'Referer':'https://www.hanmanwo.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie':'PHPSESSID=0uqatsfag6ssbng5rul475v0hn; Hm_lvt_3cf6b4fe1ac99e4aae35204f8990d09b=1583404364,1584515641; nav_switch=booklist; Hm_lpvt_3cf6b4fe1ac99e4aae35204f8990d09b=1584515704',
}
whichbook=input("请输入漫画号：")
mainurl="https://www.hanmanwo.net"
url=mainurl+"/book/"
mhdocument="mhfile"
if not os.path.exists(mhdocument):
    os.mkdir(mhdocument)
mhbook="book"+whichbook+".txt"
mhpath=mhdocument+"/"+mhbook
mhhtml=requests.get(url+whichbook).text
mhhtml.encode("utf-8")
mhlink=re.findall(r"\/chapter\/\d+",mhhtml)
mhname="测试"
for info in mhlink:
    realmhlink=mainurl+info
    print(realmhlink)
    with open(mhpath,"a")as mh:
        mh.write(realmhlink+"\n")
        mh.close()
print("写入完成")