# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
import re
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


# 上午题库入库
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


# 题目图片下载器
class QuestionImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if item['questionImg']:
            yield scrapy.Request(item['questionImg'], meta={'item': item})
        else:
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            item['questionImg'] = '/storage/images/' + "".join(image_path)
            return item


# 选项A图片下载
class OptionAImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        url = "".join(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 item['optiona']))
        if url:
            yield scrapy.Request(url, meta={'item': item})
        else:
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            item['optiona'] = 'A.' + '/storage/images/' + "".join(image_path)
            return item


# 选项B图片下载
class OptionBImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        url = "".join(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 item['optionb']))
        if url:
            yield scrapy.Request(url, meta={'item': item})
        else:
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            item['optionb'] = 'B.' + '/storage/images/' + "".join(image_path)
            return item


# 选项C图片下载
class OptionCImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        url = "".join(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 item['optionc']))
        if url:
            yield scrapy.Request(url, meta={'item': item})
        else:
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            item['optionc'] = 'C.' + '/storage/images/' + "".join(image_path)
            return item


# 选项D图片下载
class OptionDImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        url = "".join(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 item['optiond']))
        if url:
            yield scrapy.Request(url, meta={'item': item})
        else:
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            item['optiond'] = 'D.' + '/storage/images/' + "".join(image_path)
            return item


# 下午题库入库
class AfterPipeline(object):
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
        insert_sql = "insert into afternoon(question, questionImg, optionA, optionB, optionC, optionD, optionE, optionAanswer, optionAanswerImg, optionBanswer, optionBanswerImg, optionCanswer, optionCanswerImg, optionDanswer, optionDanswerImg, optionEanswer, optionEanswerImg, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item


# 题目图片下载器
class AfterQuestionImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['questionImg']):  # 判断题目中是否有图片 有则循环遍历list下载图片 否则直接返回空值
            for img_item in item['questionImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['questionImg'] = "".join(item['questionImg'])  # 巨坑 list不能直接入库(转成string)
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['questionImg'] = tempimg
            return item


# 问题一图片下载
class optionAanswerImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['optionAanswerImg']):
            for img_item in item['optionAanswerImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['optionAanswerImg'] = "".join(item['optionAanswerImg'])
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['optionAanswerImg'] = tempimg
            return item


# 问题二图片下载
class optionBanswerImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['optionBanswerImg']):
            for img_item in item['optionBanswerImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['optionBanswerImg'] = "".join(item['optionBanswerImg'])
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['optionBanswerImg'] = tempimg
            return item


# 问题三图片下载
class optionCanswerImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['optionCanswerImg']):
            for img_item in item['optionCanswerImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['optionCanswerImg'] = "".join(item['optionCanswerImg'])
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['optionCanswerImg'] = tempimg
            return item


# 问题四图片下载
class optionDanswerImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['optionDanswerImg']):
            for img_item in item['optionDanswerImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['optionDanswerImg'] = "".join(item['optionDanswerImg'])
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['optionDanswerImg'] = tempimg
            return item


# 问题五图片下载
class optionEanswerImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        file_name = item['field'] + '/' + url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        if "".join(item['optionEanswerImg']):
            for img_item in item['optionEanswerImg']:
                yield scrapy.Request(img_item, meta={'item': item})
        else:
            item['optionEanswerImg'] = "".join(item['optionEanswerImg'])
            return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            # raise DropItem("Item contains no images")
            return item
        else:
            tempimg = ''  # 对于题目多图片进行拼接合成一个字符串 (用;区分每一张图片)
            for local_img in image_path:
                tempimg += '/storage/images/' + local_img + ';'
            item['optionEanswerImg'] = tempimg
            return item

# 网络工程师上午题库入库
class wlMorningPipeline(object):

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
        insert_sql = "insert into wl_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 信息系统监理师上午题库入库
class xxMorningPipeline(object):

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
        insert_sql = "insert into xx_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 数据库系统工程师上午题库入库
class sjkMorningPipeline(object):

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
        insert_sql = "insert into sjk_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 软件评测师上午题库入库
class rjpcsMorningPipeline(object):

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
        insert_sql = "insert into rjpcs_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 嵌入式系统设计师上午题库入库
class qrsMorningPipeline(object):

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
        insert_sql = "insert into qrs_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 电子商务设计师上午题库入库
class dzswMorningPipeline(object):

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
        insert_sql = "insert into dzsw_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 多媒体应用设计师上午题库入库
class mediaMorningPipeline(object):

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
        insert_sql = "insert into media_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 信息系统管理工程师上午题库入库
class xxxtMorningPipeline(object):

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
        insert_sql = "insert into xxxt_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 信息安全工程师上午题库入库
class xxaqMorningPipeline(object):

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
        insert_sql = "insert into xxaq_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 系统集成项目管理工程师上午题库入库
class xtjcMorningPipeline(object):

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
        insert_sql = "insert into xtjc_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 系统规划与管理师上午题库入库
class xtghMorningPipeline(object):

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
        insert_sql = "insert into xtgh_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 网络规划设计师上午题库入库
class wlghMorningPipeline(object):

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
        insert_sql = "insert into wlgh_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item

# 系统架构设计师上午题库入库
class xtgjMorningPipeline(object):

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
        insert_sql = "insert into xtjg_morning(question, questionImg, optiona, optionb, optionc, optiond, answer, answeranalysis, field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
        return item