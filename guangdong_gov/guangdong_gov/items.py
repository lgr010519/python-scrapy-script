# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuangdongGovItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    publisher = scrapy.Field()
    publish_date = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    extra_link = scrapy.Field()
