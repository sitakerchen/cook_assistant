from bs4 import BeautifulSoup
from urllib.request import urlopen
from dataDefine import *
import re
import numpy as np

def updateMenu():#WEB, NAME
    dic = {}
    cnt = 0
    base_url = 'https://www.meishij.net/chufang/diy/jiangchangcaipu/?&page='
    for pages in range(1,56+1):
        html = urlopen(base_url+str(pages)).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')

        web = soup.find_all('a', 'big')
        # print(web)
        web = [str(i) for i in web]
        weblist, namelist = [], []
        re_link = re.compile(r'(http://www.*.html)')
        re_name = re.compile(r'title="(.*)"')

        for item in web:
            match_l = re_link.search(item)
            match_n = re_name.search(item)
            if match_l:
                weblist.append(match_l.group(1))
            else:
                print('fail1'.center(20, '#'))
                print(item)
            if match_n:
                namelist.append(match_n.group(1))
            else:
                match_again = re.search(r'title="【添喜的厨房】 (\w*)"', item)
                if match_again:
                    namelist.append(match_again.group(1))
                else:
                    cnt += 1
                    print(('fail'+str(cnt)).center(20, '#'))
                    print(item)
                    namelist.append('Error')
        lenth = max(len(weblist),len(namelist))
        for i in range(0, lenth):
            dic[namelist[i]] = weblist[i]
    return dic

def updateDetail(address):#raw material
    html = urlopen(address).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    body = soup.find_all('li')
    re_material = re.compile(r'target="_blank">(\w*)</a><span>(.*)</span></h4><a')
    re_material2 = re.compile(r'target="_blank">(\w*)</a></h4><span>(.*)</span><a')
    re_material3 = re.compile(r'javascript:;">(\w*)</a></h4><span>(\w*)</span><a')
    body = [str(l) for l in body]
    data = DData()
    for item in body:
        match_mater = re_material.search(item)
        match_mater2 = re_material2.search(item)
        match_mater3 = re_material3.search(item)
        if match_mater:
            data.rMaterial[match_mater.group(1)]=match_mater.group(2)
        elif match_mater2:
            data.rMaterial[match_mater2.group(1)]=match_mater2.group(2)
        elif match_mater3:
            data.rMaterial[match_mater3.group(1)]=match_mater3.group(2)
        else:
            pass
            # print('Error')
            # data.rMaterial['!']='Error'
    return data.rMaterial

def updateSteps(addr):#steps
    html = urlopen(addr).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    # print(soup.body)
    match_n = re.search(r'"step":"(\w*)步",',str(soup.body))
    total = -1
    if match_n:
        total = match_n.group(1)
    else :
        print('step not found'.center(20,'!'))
    body = soup.find_all('div','c')
    re_steps = re.compile(r'<p>(.*)</p>\s+')
    body = [str(i) for i in body]
    data = []
    for step in body:
        match_s = re_steps.search(step)
        if match_s:
            s = match_s.group(1)
            if '<img alt=' in s:
                s = re.search(r'src="(.*)"/>',s).group(1)
            data.append(s)
        else:
            pass
            # print('Not Find'.center(20,'!'))
            # print(step)
    return data,total