import scrapy


class MiddleSpider(scrapy.Spider):
    name = "middle"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.baidu.com", 'https://www.sogou.com']

    def parse(self, response):
        print(response)
