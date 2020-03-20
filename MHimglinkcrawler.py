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
    'Cookie':'PHPSESSID=008k6em59jpjtdvptfssraimdm; Hm_lvt_3cf6b4fe1ac99e4aae35204f8990d09b=1584631486; nav_switch=booklist; Hm_lpvt_3cf6b4fe1ac99e4aae35204f8990d09b=1584632201',
}
whichbook=input("输入爬取漫画号：")
mhdocument="mhfile"
mh_imgurldoc="MH-imgurl"
if not os.path.exists(mh_imgurldoc):
    os.mkdir(mh_imgurldoc)
mhbook="book"+whichbook+".txt"
linkfile=open(mhdocument+"/"+mhbook,"r")
mh_urls = linkfile.readline()
total_url=len(mh_urls)
print("漫画链接："+str(total_url))

for mh_solo_url in linkfile:
    #print(mh_solo_url)
    solo_chapter_src = requests.get(mh_solo_url)
    solo_chapter_html = solo_chapter_src.content.decode("UTF-8")
    #print(solo_chapter_html)
    all_chapter_imgname = re.findall(r"<h1 class=\"title\">(.*?)</h1>", solo_chapter_html)
    mh_bookname= BeautifulSoup.find(r"<a class=.*?>(.*?)</a>", solo_chapter_html)
    all_img_url = re.findall(r"http.*?\d+.jpg", solo_chapter_html)
    print(mh_bookname)
    for solo_chapter_imgname in all_chapter_imgname:
        print(all_chapter_imgname)
    for solo_img_url in all_img_url:
        print(solo_img_url)
    with open(mh_imgurldoc+"/"+mh_bookname+".txt") as mhbook:
        mhbook.write()
        mhbook.close()




