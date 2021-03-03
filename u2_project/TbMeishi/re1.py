import re
from bs4 import BeautifulSoup

with open('./taobao.html', 'r+', encoding='utf-8') as f:
    # print(type(f.read()))
    data = f.read().split('<body')
    # regex = re.compile('<body')


    print(data[-1])

