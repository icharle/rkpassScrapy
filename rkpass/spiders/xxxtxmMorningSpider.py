# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import xtxtxmMorningItem

# 信息系统项目管理师上午题
class XxxtxmmorningspiderSpider(scrapy.Spider):
    name = 'xxxtxmMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['593', '552', '524', '489', '457', '412', '373', '344', '325', '128', '25', '1', '11', '10', '9', '8', '7', '6', '5', '4', '3']  # 试卷的所有ID
    field_list = ['20182', '20181','20172','20171','20162','20161','20152','20151','20142','20141','20132','20131','20122','20121','20112','20111','20102','20101','20092','20091','20082']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/1_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '信息系统项目管理基础': '信息系统项目管理',
            '项目生命周期和组织': '信息系统项目管理',
            '项目管理过程': '信息系统项目管理',
            '项目立项与招投标管理': '信息系统项目管理',
            '项目整体管理': '信息系统项目管理',
            '项目范围管理': '信息系统项目管理',
            '项目进度管理': '信息系统项目管理',
            '项目成本管理': '信息系统项目管理',
            '项目质量管理': '信息系统项目管理',
            '项目人力资源管理': '信息系统项目管理',
            '项目沟通管理': '信息系统项目管理',
            '项目风险管理': '信息系统项目管理',
            '项目采购和合同管理': '信息系统项目管理',
            '文档与配置管理': '信息系统项目管理',
            '需求管理': '信息系统项目管理',
            '信息与信息化': '信息化基础知识',
            '政府信息化与电子政务': '信息化基础知识',
            '企业信息化与电子商务': '信息化基础知识',
            '信息资源管理': '信息化基础知识',
            'CIO的职责、条件和重要性': '信息化基础知识',
            'IT服务管理': '信息化基础知识',
            '新技术': '信息化基础知识',
            '信息系统': '信息系统基础',
            '信息系统建设': '信息系统基础',
            '软件工程知识': '信息系统基础',
            '软件构件技术知识': '信息系统基础',
            '软件体系结构': '信息系统基础',
            '面向对象系统分析与设计': '信息系统基础',
            '典型应用集成技术': '信息系统基础',
            '大型、复杂项目和多项目管理': '信息系统项目管理高级知识',
            '战略管理': '信息系统项目管理高级知识',
            '业务流程管理和重组': '信息系统项目管理高级知识',
            '知识管理': '信息系统项目管理高级知识',
            '项目整体绩效评估': '信息系统项目管理高级知识',
            '信息系统工程监理': '信息系统项目管理高级知识',
            '专业英语': '专业英语',
            '运筹学模型': '管理科学基础知识',
            '信息安全知识': '信息安全知识',
            '法律法规': '法律法规和标准规范',
            '软件工程的国家标准': '法律法规和标准规范',
            '综合布线标准和机房建设标准': '法律法规和标准规范',
            '网络技术标准与协议': '计算机网络基础知识',
            'Internet技术及应用': '计算机网络基础知识',
            '网络分类': '计算机网络基础知识',
            '网络管理': '计算机网络基础知识',
            '网络服务器': '计算机网络基础知识',
            '网络交换技术': '计算机网络基础知识',
            '网络存储技术': '计算机网络基础知识',
            '无线网络技术、光网络技术': '计算机网络基础知识',
            '网络接入技术': '计算机网络基础知识',
            '网络规划、设计及实施原则': '计算机网络基础知识',
            '项目管理师职业道德': '项目管理师职业道德',
        }

        # 处理分类
        # 特殊情况 题目上即为一级分类(该题库无知识点分类)
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = xtxtxmMorningItem()
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
