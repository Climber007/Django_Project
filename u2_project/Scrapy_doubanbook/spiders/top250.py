import scrapy, bs4
from ..items import ScrapyDoubanbookItem

class DoubanSpider(scrapy.Spider):
    name = "Scrapy_doubanbook"
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x*25)
        start_urls.append(url)

    def parse(self, response):
        print(response.text)

        bs = bs4.BeautifulSoup(response.text, 'lxml')
        items = bs.find_all('tr', class_='item')
        # item = ScrapyDoubanbookItem()
        for data in items:
            item = ScrapyDoubanbookItem()
            item['title'] = data.find_all('a')[1]["title"]
            item['publish'] = data.find('p', class_='pl').text
            item['score'] = data.find('span', class_='rating_nums').text
            # print(item)

            yield item


