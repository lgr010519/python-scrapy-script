from hashlib import md5
import pymysql


class ReadBookPipeline:
    # 爬虫开始前执行
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # item 就是 yield 后面的 book 对象
        self.fp.write(str(item))

        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        self.fp.close()


# 加载 settings 文件
from scrapy.utils.project import get_project_settings


class MysqlPipeline:
    effect_row = 0

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

    def process_item(self, item, spider):  # item 就是 yield 后面的 book 对象
        str = md5()
        str.update(item['src'].encode())
        encrypt_str = str.hexdigest()
        # print(encrypt_str)

        finger_sql = 'select * from book_finger where finger=%s'

        self.cursor.execute(finger_sql, [encrypt_str])
        result = self.cursor.fetchall()

        if not result:
            insert_book_sql = 'insert into book(name, src) values(%s, %s)'
            insert_finger_sql = 'insert into book_finger(finger) values(%s)'

            try:
                # 执行 sql 语句
                self.cursor.execute(insert_book_sql, [item['name'], item['src']])
                self.cursor.execute(insert_finger_sql, [encrypt_str])
                # 提交
                self.conn.commit()
                self.effect_row += 1
            except Exception as e:
                print(e)
                # 异常回滚
                self.conn.rollback()

        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        if self.effect_row > 0:
            print(f'已更新 {self.effect_row} 条数据')
        else:
            print('暂无数据更新！')

        self.cursor.close()
        self.conn.close()
