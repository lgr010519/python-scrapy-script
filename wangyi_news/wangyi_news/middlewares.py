# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class WangyiNewsDownloaderMiddleware:
    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        if request.url in spider.model_urls:
            response.text = '123'
            return response
        else:
            return response

    def process_exception(self, request, exception, spider):
        pass
