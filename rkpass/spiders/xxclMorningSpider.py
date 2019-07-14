# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import xxclMorningItem


# 信息处理技术员上午题
class XxclmorningspiderSpider(scrapy.Spider):
    name = 'xxclMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['628', '571', '534', '499', '549', '515', '451', '449', '297', '296', '207', '206', '145', '143',
                    '141', '139', '137', '135', '133', '131']  # 试卷的所有ID
    field_list = ['20191', '20181', '20172', '20171', '20162', '20161', '20152', '20151', '20142', '20141', '20132',
                  '20131', '20122', '20121', '20112', '20111', '20102', '20101', '20092', '20091']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/17_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '信息处理相关概念和术语': '信息处理技术概论',
            '信息处理技术概论': '信息处理技术概论',
            '信息处理实务': '信息处理技术概论',
            '初等数学基础': '信息处理技术概论',
            '信息与网络安全': '信息处理技术概论',
            '知识产权与标准法规': '信息处理技术概论',
            '计算机系统概论': '计算机系统基础',
            '主机系统': '计算机系统基础',
            '外部设备': '计算机系统基础',
            '计算机系统基础': '计算机系统基础',
            '软件系统': '计算机系统基础',
            '多媒体信息处理': '计算机系统基础',
            '数据压缩': '计算机系统基础',
            '电子表格处理': '电子表格处理',
            'Excel电子表格概论': '电子表格处理',
            '工作表编辑排版': '电子表格处理',
            '公式与函数': '电子表格处理',
            '数据图表与统计分析': '电子表格处理',
            'Word文字处理概论': '文字信息处理',
            '文字信息处理': '文字信息处理',
            '文本内容编辑': '文字信息处理',
            '格式排版': '文字信息处理',
            '专业英语': '专业英语',
            '其他常用操作': '文字信息处理',
            '计算机网络概论': '计算机网络基础',
            '网络设备': '计算机网络基础',
            '计算机网络基础': '计算机网络基础',
            '网络协议': '计算机网络基础',
            '网络连接': '计算机网络基础',
            '电子邮件': '计算机网络基础',
            'Internet应用': '计算机网络基础',
            'Windows操作系统': 'Windows操作系统',
            'Windows操作系统概论': 'Windows操作系统',
            'Windows基本操作': 'Windows操作系统',
            'Windows文件管理': 'Windows操作系统',
            '控制面板与其他功能': 'Windows操作系统',
            '演示文稿处理': '演示文稿处理',
            '演示文稿概论': '演示文稿处理',
            '文稿的编辑排版': '演示文稿处理',
            '动画效果设置与幻灯片放映': '演示文稿处理',
            '数据库概论': '数据库应用基础',
            'Access数据库的基本操作': '数据库应用基础',
            '信息化基础': '信息化',
            '数据结构': '计算机基础',
        }
        # 处理分类
        # 特殊情况 题目上即为一级分类(该题库无知识点分类)
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = xxclMorningItem()
        item['question'] = question
        item['questionImg'] = questionImg
        item['optiona'] = A
        item['optionb'] = B
        item['optionc'] = C
        item['optiond'] = D

        url = 'http://www.rkpass.cn/tk_jiexi.jsp?product_id=' + product_id + '&tixing=xuanze&answer=&paper_id=&tihao=&cache='
        yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True,
                             meta={'item': item, 'field': field, 'questionNum': questionNum,
                                   'knowledgeOne': knowledgeOne, 'knowledgeTwo': knowledgeTwo})

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
