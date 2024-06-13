import json
import scrapy
from guangdong_gov.items import GuangdongGovItem
import time


class GuangdongGovSpiderSpider(scrapy.Spider):
    name = "guangdong_gov_spider"

    page = 2

    def start_requests(self):
        url = 'https://www.gd.gov.cn/gkmlpt/api/all/5?page=1&sid=2'

        yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        content = json.loads(response.text)
        articles = content['articles']
        page_size = int(content['total']) // 100 + 1

        for article in articles:
            article_item = {
                'id': article['id'],
                'publisher': article['publisher'],
                'publish_date': article['display_publish_time'],
                'title': article['title']
            }
            url = article['url']

            yield scrapy.Request(url=url, callback=self.parse_detail, meta=article_item)

        if self.page <= page_size:
            url = f'https://www.gd.gov.cn/gkmlpt/api/all/5?page={str(self.page)}&sid=2'

            yield scrapy.Request(url=url, callback=self.parse_item)

            self.page += 1

    def parse_detail(self, response):
        content = ''.join(response.xpath('//div[@class="article-content"]/p/text()').extract())
        extra_link = ','.join(response.xpath('//div[@class="article-content"]/p/a/@href').extract())
        article_id = response.meta['id']
        publisher = response.meta['publisher']
        publish_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(response.meta['publish_date']))
        title = response.meta['title']
        print(title)

        article_item = GuangdongGovItem(id=article_id, publisher=publisher, publish_date=publish_date, title=title,
                                        content=content, extra_link=extra_link)

        yield article_item
