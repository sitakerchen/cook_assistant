import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'https://www.meishij.net/chufang/diy/jiangchangcaipu/'
html = urlopen(base_url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

web = soup.find_all('a', 'big')
# print(web)
web = [str(i) for i in web]
weblist, namelist = [], []
re_link = re.compile(r'(http://www.*.html)')
re_name = re.compile(r'title="(\w*)"')

for item in web:
    match_l = re_link.search(item)
    match_n = re_name.search(item)
    if match_l:
        weblist.append(match_l.group(1))
    else:
        print('fail1'.center(20,'#'))
        print(item)
    if match_n:
        namelist.append(match_n.group(1))
    else:
        match_again = re.search(r'title="【添喜的厨房】 (\w*)"',item)
        if match_again:
            namelist.append(match_again.group(1))
        else:
            print('fail2'.center(20, '#'))
dic = {}
for i in range(0, len(weblist)-1):
    dic[namelist[i]]=weblist[i]

