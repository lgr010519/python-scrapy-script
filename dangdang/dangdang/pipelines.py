# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 需先在 settings.py 文件中开启管道
# class DangdangPipeline:
#     # 爬虫开始前执行
#     def open_spider(self, spider):
#         self.fp = open('book.json', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):  # item 就是 yield 后面的 book 对象
#
#         # 以下方法不推荐，对文件操作过于频繁
#         # with open('book.json', 'a', encoding='utf-8') as fp:  # w 模式会每一个对象都打开一次文件，覆盖前面的内容
#         #     fp.write(str(item))  # write 方法要传字符串
#
#         self.fp.write(str(item))
#
#         return item
#
#     # 爬虫结束后执行
#     def close_spider(self, spider):
#         self.fp.close()


# 开启多条管道
#     1.定义管道类
#     2.在 settings 中开启管道
# class DangdangDownloadPipeline:
#     def process_item(self, item, spider):
#         url = 'http:' + item.get('src')
#         filename = './books/' + item.get('name') + '.jpg'
#
#         urllib.request.urlretrieve(url=url, filename=filename)
#
#         return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DangdangDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = 'http:' + item['src']
        yield scrapy.Request(url=url, meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        book = request.meta['item']
        book_name = book['name']
        return book_name

    def item_completed(self, results, item, info):
        return item
