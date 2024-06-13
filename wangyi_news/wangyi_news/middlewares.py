# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from time import sleep
from scrapy.http import HtmlResponse


class WangyiNewsDownloaderMiddleware:
    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        if request.url in spider.model_urls:
            driver = spider.driver
            driver.get(request.url)

            sleep(2)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)

            print(driver.page_source)

            return HtmlResponse(url=request.url, body=driver.page_source, encoding='utf-8', request=request)
        else:
            return response

    def process_exception(self, request, exception, spider):
        pass
