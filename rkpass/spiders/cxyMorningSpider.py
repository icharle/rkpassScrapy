# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import cxyMorningItem

# 程序员上午题
class CxymorningspiderSpider(scrapy.Spider):
    name = 'cxyMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['599', '581', '528', '497', '467', '512', '442', '441', '299', '298', '204', '202', '126', '124', '122', '120', '118', '116', '114', '112']  # 试卷的所有ID
    field_list = ['20182', '20181','20172','20171','20162','20161','20152','20151','20142','20141','20132','20131','20122','20121','20112','20111','20102','20101','20092','20091']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/15_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
                field_list[j] + '&questionNum=' + str(i))

    def parse(self, response):
        questionNum = str(response.url).strip().split("questionNum=")[-1]  # 题号 scrapy运行插库顺序不一致问题
        field = (str(response.url).strip().split("field=")[-1]).split("&")[0]  # 区别场次 20181表示2018年上半年
        knowledgeTwo = response.xpath(".//span[@class='red']//text()").extract()  # 知识点(二级分类)
        # 针对题库无分类处理
        knowledgeTwo = knowledgeTwo[0] if list(knowledgeTwo) else ""
        dataimg = response.xpath(".//span[@class='shisi_text']/img[last()]/@src").extract()  # 爬取题目及选项中图片
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

        info = {
            '软件工程和项目管理基础知识': '软件开发和运行维护基础知识',
            '系统分析与系统设计基础知识': '软件开发和运行维护基础知识',
            '程序设计基础知识': '软件开发和运行维护基础知识',
            '程序测试基础知识': '软件开发和运行维护基础知识',
            '软件开发文档基础知识': '软件开发和运行维护基础知识',
            '软件运行和维护基础知识': '软件开发和运行维护基础知识',
            '面向对象技术': '软件开发和运行维护基础知识',
            '统一建模语言(UML)': '软件开发和运行维护基础知识',
            '算法设计概述': '数据结构与算法',
            '线性表': '数据结构与算法',
            '树和二叉树': '数据结构与算法',
            '图': '数据结构与算法',
            '排序与查找': '数据结构与算法',
            '递归法': '数据结构与算法',
            '数据结构基础': '数据结构与算法',
            '矩阵': '数据结构与算法',
            '数制及其转换': '计算机硬件基础知识',
            '数据的表示': '计算机硬件基础知识',
            '算术运算和逻辑运算': '计算机硬件基础知识',
            '计算机系统的组成': '计算机硬件基础知识',
            '计算机类型和特点': '计算机硬件基础知识',
            '中央处理器CPU': '计算机硬件基础知识',
            '输入/输出及通信设备': '计算机硬件基础知识',
            '存储器系统': '计算机硬件基础知识',
            '汇编系统基本原理': '程序语言基础知识',
            '编译系统基本原理': '程序语言基础知识',
            '解释系统基本原理': '程序语言基础知识',
            '程序语言的数据类型': '程序语言基础知识',
            '程序语言的控制结构': '程序语言基础知识',
            '程序语言基础': '程序语言基础知识',
            'HTML语言': '程序语言基础知识',
            '处理机管理（进程管理）': '操作系统基础知识',
            '存储管理': '操作系统基础知识',
            '操作系统的功能、类型和层次结构': '操作系统基础知识',
            '设备管理': '操作系统基础知识',
            '文件管理': '操作系统基础知识',
            '作业管理': '操作系统基础知识',
            '网络操作系统': '操作系统基础知识',
            '嵌入式操作系统': '操作系统基础知识',
            '网络的功能、分类与组成': '网络基础知识',
            '网络协议与标准': '网络基础知识',
            '网络结构与通信': '网络基础知识',
            '三层结构': '网络基础知识',
            'Internet和Intranet初步': '网络基础知识',
            '网络安全': '网络基础知识',
            '数据库管理系统的功能和特征': '数据库系统',
            '数据库模型': '数据库系统',
            '数据模型': '数据库系统',
            '数据操作': '数据库系统',
            '数据库语言': '数据库系统',
            '数据库的控制功能': '数据库系统',
            'Windows基本操作': '计算机应用基础知识',
            '办公自动化': '计算机应用基础知识',
            '电子邮件': '计算机应用基础知识',
            '浏览器': '计算机应用基础知识',
            '信息处理实务': '计算机应用基础知识',
            '专业英语': '专业英语',
            '应用数学': '	应用数学',
            '著作权法及实施条例': '	软件的知识产权保护',
            '计算机软件保护条例': '	软件的知识产权保护',
            '商标法及实施条例': '软件的知识产权保护',
            '专利法及实施细则': '软件的知识产权保护',
            '反不正当竞争法': '软件的知识产权保护',
            '多媒体技术基本概念': '多媒体技术及其应用',
            '数据压缩技术': '多媒体技术及其应用',
            '图形图像': '多媒体技术及其应用',
            '音频': '多媒体技术及其应用',
            '视频': '多媒体技术及其应用',
            '数据安全与保密': '信息安全与系统性能指标',
            '计算机病毒的防治': '信息安全与系统性能指标',
            '计算机木马的防治': '信息安全与系统性能指标',
            '系统性能指标': '信息安全与系统性能指标',
            '标准化概述': '标准化知识',
            '标准的层次': '标准化知识',
            '标准的编码': '标准化知识',
            '标准化机构': '标准化知识',
            '信息安全标准': '标准化知识',
            '软件开发规范和文档标准': '标准化知识',
            'ISO9000标准': '标准化知识',
        }
        # 处理分类
        # 特殊情况 题目上即为一级分类(该题库无知识点分类)
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = cxyMorningItem()
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
