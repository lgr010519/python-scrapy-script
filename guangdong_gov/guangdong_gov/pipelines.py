# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GuangdongGovPipeline:
    # 爬虫开始前执行
    def open_spider(self, spider):
        self.fp = open('articles.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))

        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        self.fp.close()


# 加载 settings 文件
from scrapy.utils.project import get_project_settings


class MysqlPipeline:
    # 爬虫开始前执行
    def open_spider(self, spider):
        settings = get_project_settings()

        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset,
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = ('insert into news(id, publisher,publish_date,title,content,extra_link) values("{}", "{}", "{}", "{}", '
               '"{}", "{}")').format(
            item['id'], item['publisher'], item['publish_date'], item['title'], item['content'], item['extra_link'])

        try:
            # 执行 sql 语句
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()
        except Exception as e:
            print(e)
            # 异常回滚
            self.conn.rollback()

        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
