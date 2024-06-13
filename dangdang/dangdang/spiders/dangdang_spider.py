import scrapy

from dangdang.items import DangdangItem


class DangdangSpiderSpider(scrapy.Spider):
    name = "dangdang_spider"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.03.00.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # src = '//ul[@id="component_59"]/li//img/@src'
        # name = '//ul[@id="component_59"]/li/p[@class="name"]/a/text()'
        # price = '//ul[@id="component_59"]/li/p[@class="price"]/span[@class="search_now_price"]/text()'

        # src = response.xpath('//ul[@id="component_59"]/li/a/img/@data-original')
        # name = response.xpath('//ul[@id="component_59"]/li/p[@class="name"]/a/text()')
        # price = response.xpath('//ul[@id="component_59"]/li/p[@class="price"]/span[@class="search_now_price"]/text()')

        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            src = li.xpath('./a/img/@data-original').get() or li.xpath('./a/img/@src').get()
            name = li.xpath('./p[@class="name"]/a/text()').get()
            price = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').get()

            # print(li_src)

            book = DangdangItem(src=src, name=name, price=price)

            yield book

        if self.page < 3:
            self.page += 1
            url = f'{self.base_url}{str(self.page)}-cp01.03.00.00.00.00.html'
            yield scrapy.Request(url=url, callback=self.parse)
