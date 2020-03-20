import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
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
whichbook=input("输入爬取漫画号：")
osdir="C:/Users/Administrator/PycharmProjects/untitled/"
mhdocument="mhfile"
mhbook="book"+whichbook+".txt"
linkfile=open(osdir+mhdocument+"/"+mhbook,"r")
mh_urls = linkfile.readline()
total_url=len(mh_urls)
print("漫画链接："+str(total_url))
#for mh_solo_url in mh_urls:
 ##   mh_url_src=requests.get(mh_solo_url_str).content
   # print(mh_url_src)




