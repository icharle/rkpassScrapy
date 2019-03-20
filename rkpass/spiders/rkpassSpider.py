# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import RkpassItem

# 软件设计师上午题
class RkpassspiderSpider(scrapy.Spider):
    name = 'rkpassSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['592', '553', '519', '485', '463', '420', '378', '359', '305', '304', '91', '89', '72', '74', '76', '78',
                    '80', '82', '84', '88']   # 试卷的所有ID
    field_list = ['20182', '20181', '20172', '20171', '20162', '20161', '20152', '20151', '20142', '20141', '20132', '20131',
                  '20122', '20121', '20112', '20111', '20102', '20101', '20092', '20091']    # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/6_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
                field_list[j] + '&questionNum=' + str(i))

    def parse(self, response):
        questionNum = str(response.url).strip().split("questionNum=")[-1]  # 题号 scrapy运行插库顺序不一致问题
        field = (str(response.url).strip().split("field=")[-1]).split("&")[0]  # 区别场次 20181表示2018年上半年
        dataimg = response.xpath(".//span[@class='shisi_text']/img[last()]/@src").extract()  # 爬取题目及选项中图片
        knowledgeTwo = response.xpath(".//span[@class='red']//text()").extract()[0]  # 知识点(二级分类)
        product_id = re.findall('\((.*?)\)', response.xpath(".//script//text()").extract()[0])[0].split(',')[0].strip(
            "'")  # 该题目id 用于整理答案
        question = "".join(response.xpath(".//table/tr[2]/td/span[@class='shisi_text']//text()").extract())  # 题目
        A = "".join(
            "".join(response.xpath(".//table/tr[5]/td/span[@class='shisi_text']//text()").extract()).split())  # A选项
        B = "".join(
            "".join(response.xpath(".//table/tr[7]/td/span[@class='shisi_text']//text()").extract()).split())  # B选项
        C = "".join(
            "".join(response.xpath(".//table/tr[9]/td/span[@class='shisi_text']//text()").extract()).split())  # C选项
        D = "".join(
            "".join(response.xpath(".//table/tr[11]/td/span[@class='shisi_text']//text()").extract()).split())  # D选项

        questionImg = ''  # 初始化 防止插库失败
        if len(dataimg) > 0:  # 判断题目及选项中是否有图片
            if len(dataimg) == 1:
                questionImg = dataimg[0]  # 第一张为题目图片
            elif len(dataimg) == 4:  # 图片总数等于4张 即为选项中图片
                A = A + dataimg[0]
                B = B + dataimg[1]
                C = C + dataimg[2]
                D = D + dataimg[3]
            elif len(dataimg) == 5:  # 图片总数等于5张 则分别是A、B、C、D中的图片
                questionImg = dataimg[0]  # 第一张为题目图片
                A = A + dataimg[1]
                B = B + dataimg[2]
                C = C + dataimg[3]
                D = D + dataimg[4]

        # 处理分类
        info = {
            '计算机基本工作原理': '计算机组成与结构',
            '存储系统': '计算机组成与结构',
            '输入输出系统': '计算机组成与结构',
            '总线系统': '计算机组成与结构',
            '指令系统和计算机体系结构': '计算机组成与结构',
            '系统性能评测和可靠性基础': '计算机组成与结构',
            '信息安全和病毒防护': '计算机组成与结构',
            '面向对象的基本概念': '面向对象技术',
            '面向对象程序设计': '面向对象技术',
            '面向对象开发技术': '面向对象技术',
            '面向对象分析与设计方法': '面向对象技术',
            '设计模式': '面向对象技术',
            '线性结构': '算法与数据结构',
            '数组、矩阵和广义表': '算法与数据结构',
            '树': '算法与数据结构',
            '图': '算法与数据结构',
            '查找算法': '算法与数据结构',
            '排序算法': '算法与数据结构',
            '算法分析及常用算法': '算法与数据结构',
            '结构化分析和设计': '系统开发与运行',
            '系统设计知识': '系统开发与运行',
            '系统的测试与维护': '系统开发与运行',
            '数据库基础知识': '数据库技术',
            'E-R模型': '数据库技术',
            'E-R模型和关系模型': '数据库技术',
            '关系代数和关系模型': '数据库技术',
            '关系代数': '数据库技术',
            'SQL语言': '数据库技术',
            '关系数据库的规范化': '数据库技术',
            '控制功能': '数据库技术',
            '操作系统定义、分类及功能': '操作系统',
            '进程管理': '操作系统',
            '存储管理': '操作系统',
            '设备管理': '操作系统',
            '文件管理': '操作系统',
            '作业管理': '操作系统',
            '软件工程概述': '软件工程基础知识',
            '软件开发项目管理': '软件工程基础知识',
            '软件工具与开发环境': '软件工程基础知识',
            '软件过程管理': '软件工程基础知识',
            '软件质量管理': '软件工程基础知识',
            '程序设计语言基本概念': '程序语言',
            '汇编、编译、解释系统': '程序语言',
            '文法分析': '程序语言',
            'ISO／OSI网络体系结构': '网络与多媒体基础知识',
            '网络互连硬件': '网络与多媒体基础知识',
            '网络协议': '网络与多媒体基础知识',
            'Internet应用': '网络与多媒体基础知识',
            '网络安全': '网络与多媒体基础知识',
            '声音及其数字化': '网络与多媒体基础知识',
            '图形和图像': '网络与多媒体基础知识',
            '动画与视频': '网络与多媒体基础知识',
            '多媒体计算机': '网络与多媒体基础知识',
            '多媒体网络': '网络与多媒体基础知识',
            '专业英语': '专业英语',
            '标准化': '标准化和知识产权',
            '知识产权': '标准化和知识产权',
        }

        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = RkpassItem()
        item['question'] = question
        item['questionImg'] = questionImg
        item['optiona'] = A
        item['optionb'] = B
        item['optionc'] = C
        item['optiond'] = D

        url = 'http://www.rkpass.cn/tk_jiexi.jsp?product_id=' + product_id + '&tixing=xuanze&answer=&paper_id=&tihao=&cache='
        yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True, meta={'item': item, 'field': field, 'questionNum': questionNum, 'knowledgeOne': knowledgeOne, 'knowledgeTwo': knowledgeTwo})

    def parse_detail(self, response):
        knowledgeOne = response.meta['knowledgeOne']  # 接收当前题目一级分类
        knowledgeTwo = response.meta['knowledgeTwo']  # 接收当前题目二级分类
        questionNum = response.meta['questionNum']  # 接收当前题目号
        field = response.meta['field']  # 接收当前考试场次
        item = response.meta['item']  # 接收上级已爬取的数据
        answer = response.xpath(".//td/span[@class='shisi_text']//text()").extract()[2].strip()  # 答案
        answerAnalysis = response.xpath(".//table/tr[3]/td//text()").extract()  # 答案解析
        answerAnalysis = "".join(answerAnalysis[3:len(answerAnalysis)])

        # 接收二级答案页面数据
        item['answer'] = answer
        item['answeranalysis'] = answerAnalysis
        item['field'] = field
        item['questionNum'] = questionNum
        item['knowledgeOne'] = knowledgeOne
        item['knowledgeTwo'] = knowledgeTwo

        return item
