# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import xxMorningItem

# 信息系统监理师
class XxmorningspiderSpider(scrapy.Spider):
    name = 'xxMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['604', '563', '530', '506', '460', '422', '394', '348', '312', '311', '218', '216', '184', '182', '180', '178',
                    '176', '174', '172']   # 试卷的所有ID
    field_list = ['20182', '20181', '20172', '20171', '20162', '20161', '20152', '20151', '20142', '20141', '20132', '20131',
                  '20122', '20121', '20112', '20111', '20102', '20101', '20091']    # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/8_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
                field_list[j] + '&questionNum=' + str(i))

    def parse(self, response):
        questionNum = str(response.url).strip().split("questionNum=")[-1]  # 题号 scrapy运行插库顺序不一致问题
        field = (str(response.url).strip().split("field=")[-1]).split("&")[0]  # 区别场次 20181表示2018年上半年
        knowledgeTwo = response.xpath(".//span[@class='red']//text()").extract()[0]  # 知识点(二级分类)
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

        # 处理分类
        info = {
            '信息系统工程监理概念': '信息系统工程监理知识',
            '信息系统工程监理依据': '信息系统工程监理知识',
            '监理单位的组织建设': '信息系统工程监理知识',
            '监理工作的组织和规划': '信息系统工程监理知识',
            '质量控制': '信息系统工程监理知识',
            '进度控制': '信息系统工程监理知识',
            '投资控制': '信息系统工程监理知识',
            '变更控制': '信息系统工程监理知识',
            '合同管理': '信息系统工程监理知识',
            '安全管理': '信息系统工程监理知识',
            '信息管理': '信息系统工程监理知识',
            '沟通协调': '信息系统工程监理知识',
            '信息系统监理师职业道德要求': '信息系统工程监理知识',
            '信息系统建设': '信息系统工程技术知识',
            '计算机技术知识与网络知识': '信息系统工程技术知识',
            '信息网络系统': '信息系统工程技术知识',
            '软件与软件工程知识': '信息系统工程技术知识',
            '专业英语': '专业英语',
            '信息工程项目管理知识': '项目管理基础知识',
            '项目管理基础知识': '项目管理基础知识',
        }
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = xxMorningItem()
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