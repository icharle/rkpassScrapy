# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class RkpassPipeline(object):

    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        insert_sql = "insert into morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item
