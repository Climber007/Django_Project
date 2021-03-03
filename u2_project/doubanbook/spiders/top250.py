import scrapy, bs4
from ..items import DoubanbookItem

class Doubanbook(scrapy.Spider):
    '''输入网址，调度器调度'''
    name = 'doubanbook'
    allowed_domains = 'douban.com'
    start_urls = []
    for i in range(3):
        start_urls.append('https://book.douban.com/top250?start='+str(i*25))

    def parse(self, response):
        '''解析数据'''
        bs = bs4.BeautifulSoup(response.text, 'lxml')
        items = bs.find_all('tr', class_='item')
        item = DoubanbookItem()
        for data in items:
            # item = DoubanbookItem()
            item['title'] = data.find_all('a')[1]["title"]
            item['publish'] = data.find('p', class_='pl').text
            item['score'] = data.find('span', class_='rating_nums').text
            # print(item)
            yield item
