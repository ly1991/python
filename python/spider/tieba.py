# -*- coding:utf-8 -*-
import requests,urllib,time,os
from bs4 import BeautifulSoup

def downImgs(url,pages,path):
    # 保存路径拼接
    now = time.strftime('%Y%m%d_%H.%M.%S', time.localtime(time.time()))
    savePath = path + '\\' + now + '\\'
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    print('保存路径为：'+savePath)
    for page in range(pages):
        #拼接url
        downUrl = url + str(page)
        #发起请求
        r = requests.get(downUrl)
        #解析并且格式化页面
        soup = BeautifulSoup(r.content, "html.parser")
        #获取页面图片
        imgs = soup.find_all('img',attrs={'class':'BDE_Image'})
        for img in imgs:
            src = img['src']
            imgName= src[src.rfind('/'):]
            urllib.request.urlretrieve(src, savePath+'%s' % imgName)
            print(imgName[1:]+'   finished……')
        print('done……')

url = 'https://tieba.baidu.com/p/xxxxxxx?see_lz=1&pn='
downImgs(url,1,'D:\E')

