# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddlewareTestDownloaderMiddleware:
    # 拦截所有请求
    def process_request(self, request, spider):
        print('process_request')
        # 伪装请求头
        # request.headers['User-Agent'] = 'xxx'
        # request.headers['Cookie'] = 'xxx'
        return None

    # 拦截响应对象
    def process_response(self, request, response, spider):
        print('process_response')
        return response

    # 拦截异常请求
    def process_exception(self, request, exception, spider):
        # 请求ip被禁用，该请求就变成异常请求
        # request.meta['proxy'] = 'http://ip:port'  # 设置代理
        print('process_exception')
        return request  # 将异常请求修正后重新发送
