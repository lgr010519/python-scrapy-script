import json

import scrapy


class JuejinSpiderSpider(scrapy.Spider):
    name = "juejin_spider"

    # allowed_domains = ["www.xxx.com"]
    # start_urls = [
    #     "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?aid=2608&uuid=7304087339705402891&spider=0"]

    def start_requests(self):
        url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?aid=2608&uuid=7304087339705402891&spider=0'

        form_data = {
            'client_type': '2608',
            'cursor': "1",
            'id_type': '2',
            'limit': '20',
            'sort_type': '200'
        }

        yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        articles = json.loads(response.text)['data']

        title = None
        cover_image = None
        url = None

        for article in articles:
            if 'article_info' in article['item_info']:
                title = article['item_info']['article_info']['title']
                cover_image = article['item_info']['article_info']['cover_image']
                url = f'https://juejin.cn/post/{article['item_info']['article_info']['article_id']}'
            else:
                title = article['item_info']['title']
                url = article['item_info']['url']

            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        content = response.text
        print(content)
