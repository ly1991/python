# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/'


ck = open(r'cookie.txt','r')
cookies = {}
for line in ck.read().split(';'):
    name,value = line.strip().split('=',1)
    cookies[name] = value


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'d_c0="ADACw8cKSwuPTtmJ9pgSZYiNxncnydQhw4M=|1486794551"; _zap=74134c90-4230-49ea-9c8f-352e78fa2b84; q_c1=1e2294db7c60428fa13ef9e0171beb0b|1493292419000|1486794551000; r_cap_id="NzJhZTlkZmEzMmJkNGI2YjljMjQ5ZDZlMWUwM2UwMTA=|1494335372|953968d73c9d773b2fdbe1a3ba589a327fff2daa"; cap_id="Mjk3ZTJmMDg2MTg4NDg2ZGIxMmRlNTNiYWVhM2NjNTA=|1494335372|e619ed9c7ca7e2ae2319d696d1778b50dc3c7872"; aliyungf_tc=AQAAANFIw0MxYQgAb+NZddNgLMMm+074; acw_tc=AQAAAC4KfxhPjwkAb+NZdYu6AAhwwBpI; _xsrf=c0a7c5eb3aa3e1181eced32a3404c92e; __utma=51854390.1609703722.1486794560.1494335398.1494658346.11; __utmb=51854390.0.10.1494658346; __utmc=51854390; __utmz=51854390.1486881195.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20140220=1^3=entry_date=20140220=1; z_c0=Mi4wQUFBQWRIOG1BQUFBTUFMRHh3cExDeGNBQUFCaEFsVk5ra3c1V1FDd2phaVNzYUh3SkszLTRZaXNjRmt1U05wVm1R|1494659129|dd76d92e23f15e28f90d1af834fc4da2b6ef5fd2',
    'Host':'www.zhihu.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

r= requests.get(url,headers = headers)
soup = BeautifulSoup(r.content,'html.parser')
print(soup.prettify())