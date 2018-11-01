# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RkpassItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试


# class rkpassAfterItem(scrapy.Item):
#     question = scrapy.Field()  # 题目
#     questionImg = scrapy.Field()  # 题目图片
#     optionA = scrapy.Field()  # 题目问题
#     optionB = scrapy.Field()  # 题目问题
#     optionC = scrapy.Field()  # 题目问题
#     optionD = scrapy.Field()  # 题目问题
#     optionE = scrapy.Field()  # 题目问题
