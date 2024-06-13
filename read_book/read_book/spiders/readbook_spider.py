import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from read_book.items import ReadBookItem


class ReadbookSpiderSpider(CrawlSpider):
    name = "readbook_spider"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1617_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1617_\d+\.html"), callback="parse_item", follow=False),)

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@alt').get()
            src = img.xpath('./@data-original').get()

            book = ReadBookItem(name=name, src=src)

            yield book
