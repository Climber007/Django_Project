from lxml import etree
from bs4 import BeautifulSoup

from pyquery import PyQuery as pq

with open('./taobao.html', 'r+', encoding='utf-8') as f:
    html = f.read().split('<body')[-1]
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    items = soup.find_all('div', class_='item J_MouserOnverReq')
    if not items:
        print('数据为空')
    i = 0
    for item in items:
        products = {
            'title': item.find('div', class_='row row-2 title').text.strip(),
            'deal': item.find('div', class_='deal-cnt').text[:-3],
            'price': item.find('div', class_='price g_price g_price-highlight').text.strip(),
            'shop': item.find('div', class_='shop').text.strip(),
            'location': item.find('div', class_='location').text,
            'image': item.find('img', class_='J_ItemPic img')['data-src'],
        }
        i+=1
        print(products)

    print(i)
    print('-'*30)


    # title = soup.select('#J_Itemlist_TLink_570663818285')
    # print(title)


    # root = etree.HTML(str(f))
    # titles = root.xpath('//*[@class="J_ClickStat"]/text()[1]')
    # for title in titles:
    #     print(title)




    # items = soup.find_all('div', class_='item J_MouserOnverReq  ')
    # print(items)
    # for item in items:
    #     products = {
    #         'image': item.find('img').attr('src'),
    #         'deal': (item.find('div', class_='deal-cnt').text)[:-3],
    #         'price': item.find('div', class_='price g_price g_price-highlight').text,
    #         'title': item.find('div', class_='row row-2 title').text,
    #         'shop': item.find('div', class_= 'shop').text,
    #         'location': item.find('div', class_='location').text
    #     }
    #     print(products)

