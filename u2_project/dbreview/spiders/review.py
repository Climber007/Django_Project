import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DbreviewItem
from scrapy_redis.spiders import RedisCrawlSpider

class ReviewSpider(RedisCrawlSpider):
    name = 'review'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/26357307/reviews']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item = DbreviewItem()
        item['comment'] = response.xpath('//div[@class="short-content"]/text()').extract_first() # 取lst中第一个元素
        print(dict(item), '++++++++++++++++++++++++++++++')
        yield item


sorted()