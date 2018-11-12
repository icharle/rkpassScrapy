# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 软件设计师上午题
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

# 软件设计师下午题
class rkpassAfterItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optionA = scrapy.Field()  # 题目问题
    optionB = scrapy.Field()  # 题目问题
    optionC = scrapy.Field()  # 题目问题
    optionD = scrapy.Field()  # 题目问题
    optionE = scrapy.Field()  # 题目问题
    optionAanswer = scrapy.Field()  # 题目答案
    optionAanswerImg = scrapy.Field()  # 图片题目答案
    optionBanswer = scrapy.Field()  # 题目答案
    optionBanswerImg = scrapy.Field()  # 图片题目答案
    optionCanswer = scrapy.Field()  # 题目答案
    optionCanswerImg = scrapy.Field()  # 图片题目答案
    optionDanswer = scrapy.Field()  # 题目答案
    optionDanswerImg = scrapy.Field()  # 图片题目答案
    optionEanswer = scrapy.Field()  # 题目答案
    optionEanswerImg = scrapy.Field()  # 图片题目答案
    field = scrapy.Field()  # 场次

# 网络工程师上午题
class wlMorningItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试

# 信息系统监理师上午题
class xxMorningItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试

# 数据库系统工程师上午题
class sjkMorningItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试

# 软件评测师上午题
class rjpcsMorningItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试

# 嵌入式系统设计师上午题
class qrsMorningItem(scrapy.Item):
    question = scrapy.Field()  # 题目
    questionImg = scrapy.Field()  # 题目图片
    optiona = scrapy.Field()  # 选项A
    optionb = scrapy.Field()  # 选项B
    optionc = scrapy.Field()  # 选项C
    optiond = scrapy.Field()  # 选项D
    answer = scrapy.Field()  # 答案
    answeranalysis = scrapy.Field()  # 答案解析
    field = scrapy.Field()  # 考试场次 20181代表2018上半年考试