#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
import time

import requests
from bs4 import BeautifulSoup
from urllib.request import quote

search = input('请输入关键词：')
kwen = search.encode('utf-8') #将汉字，用utf格式编码，赋值给gbkkw
f = open('Sciencedirect.txt', 'w', encoding ='utf-8') #创建txt格式文件，方便等会存储
#添加请求头，模拟浏览器正常访问，避免被反爬虫
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for x in range(4): #想要爬取多少页数据
    #time.sleep(10)
    #https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=TCM%20treatment&highlight=true&returnType=SEARCH&matchPubs=true&pageNumber=1&returnFacets=ALL
    #https: // www.sciencedirect.com / search?qs = TCM & offset = 50
    url = 'https://www.sciencedirect.com/search?qs='+quote(kwen)+'&offset='+str(x*10)
    res = requests.get(url,headers = headers)
    print(res.status_code) #查看是否能获取数据
    bs1 = BeautifulSoup(res.text, 'html.parser') #解析数据
    list_titles = bs1.find_all('div', class_="result-item-content")
    #print(list_titles)
    for i in list_titles:
        title = i.find('h2').text  # 爬到标题
        print(title)
        f.write("题目："+title.strip())
        f.write('\n')
        #获取文章跳转链接
        half_link = i.find('h2').find('span').find('a')['href']
        wholelink = 'https://www.sciencedirect.com'+str(half_link)
        re = requests.get(wholelink, headers=headers) #爬取该网站内容
        if re.status_code == 200:
            bs2 = BeautifulSoup(re.text, 'html.parser') #解析该网站内容
            #摘要
            if bs2.find('div',class_="abstract author")!=None:
                infos = bs2.find('div',class_="abstract author")
                if infos.find('p')!=None:
                    abstract = infos.find('p').text.strip()
                    print(abstract)
                    f.write("摘要： "+abstract)
                    f.write('\n')
                else:
                    f.write("摘要为空")
                    f.write('\n')
            else:
                f.write("摘要为空")
                f.write('\n')

            #关键字
            if bs2.find('div',class_="Keywords u-font-serif")!=None:
                infos = bs2.find('div',class_="Keywords u-font-serif")
                if infos.find('div')!=None:
                    keywords = infos.find('div').text.strip()
                    keywords=keywords.replace("Keywords","")
                    keywords=keywords.replace("Abbreviations", "")
                    keywords = keywords.replace("Key words", "")
                    print(keywords)
                    f.write("关键字： "+keywords)
                    f.write('\n')
                else:
                    f.write("关键字为空")
                    f.write('\n')
            else:
                f.write("关键字为空")
                f.write('\n')

            #其他信息
            if bs2.find('div',class_="text-xs")!=None:
                infos = bs2.find('div',class_="text-xs").text.strip()
                print(infos)
                f.write("其他信息： "+infos)
                f.write('\n')
            else:
                f.write("其他信息为空")
                f.write('\n')

            #作者
            if bs2.find('div', class_="author-group") != None:
                infos = bs2.find('div', class_="author-group").text.strip()
                infos=infos.replace("Author links open overlay panel","")
                print(infos)
                f.write("作者： " + infos)
                f.write('\n')
            else:
                f.write("作者为空")
                f.write('\n')

            #链接
            if bs2.find('a', class_="doi") != None:
                infos = bs2.find('a', class_="doi").text.strip()
                print(infos)
                f.write("链接： " + infos)
                f.write('\n')
            else:
                f.write("链接为空")
                f.write('\n')

            f.write('\r\n')

f.close()
