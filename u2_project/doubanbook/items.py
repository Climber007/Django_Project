# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanbookItem(scrapy.Item):
    '''构造 爬取数据类'''
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publish = scrapy.Field()
    score = scrapy.Field()