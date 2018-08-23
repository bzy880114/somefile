# coding=utf-8
"""根据搜索词下载百度图片"""
import urllib.request
#import re
import requests
 
def getDatas(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': '',
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': '',
                      'istype': '',
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1535007423240': ''
                  })
    url = 'https://image.baidu.com/search/index'
    urls = []

    
    for i in params:
        #rep = requests.get(url, headers={'user-Agent': userAgent}, params=params)
        try:
            urls.append(requests.get(url,params=i).json().get('data'))
        except Exception as e:
            print(e)        
    return urls
 
def getImg(datalist,path):
    x=0
    for list in datalist:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                urllib.request.urlretrieve(i.get('thumbURL'), path+'%d.jpg'%x)
                x += 1
            else:
                print('图片链接不存在')
 
 
if __name__ == '__main__':
    datalist=getDatas('工地工人',100)
    getImg(datalist, 'E:/Video/scrapy2/')