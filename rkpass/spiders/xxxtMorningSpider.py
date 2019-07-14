# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import xxxtMorningItem

# 信息系统管理工程师上午题
class XxxtmorningspiderSpider(scrapy.Spider):
    name = 'xxxtMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['629', '569', '500', '427', '350', '310', '261', '260', '259', '257']  # 试卷的所有ID
    field_list = ['20191', '20181', '20171', '20161', '20151', '20141', '20131', '20121', '20111',
                  '20092']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/9_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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

        info = {
            '软件工程基础': '软件工程',
            '数据库技术基础': '数据库技术',
            '关系数据库的数据操作': '数据库技术',
            '数据库管理系统': '数据库技术',
            '资源管理概述': '资源管理',
            '硬件管理': '资源管理',
            '软件管理、软件著作权、商标': '资源管理',
            '网络资源管理': '资源管理',
            '数据管理': '资源管理',
            '设施和设备管理': '资源管理',
            '计算机基本组成': '计算机硬件基础',
            '计算机的系统结构': '计算机硬件基础',
            '计算机存储系统': '计算机硬件基础',
            '计算机应用领域': '计算机硬件基础',
            '网络的基础知识': '网络基础知识',
            '计算机网络体系结构与协议': '网络基础知识',
            '计算机网络传输': '网络基础知识',
            '计算机局域网': '网络基础知识',
            '网络的管理与管理软件': '网络基础知识',
            '网络安全': '网络基础知识',
            '网络性能分析与评估': '网络基础知识',
            '因特网基础知识及其应用': '网络基础知识',
            '专业英语': '专业英语',
            '系统性能评价': '性能及能力管理',
            '系统能力管理': '性能及能力管理',
            '信息系统概述': '信息系统开发的基础知识',
            '信息系统工程概述': '信息系统开发的基础知识',
            '信息系统开发概述': '信息系统开发的基础知识',
            '信息系统项目': '信息系统开发的管理知识',
            '信息系统中的项目管理': '信息系统开发的管理知识',
            '信息系统开发的管理工具': '信息系统开发的管理知识',
            '操作系统简介': '操作系统知识',
            '处理机管理': '操作系统知识',
            '存储管理': '操作系统知识',
            '设备管理': '操作系统知识',
            '文件管理': '操作系统知识',
            '作业管理': '操作系统知识',
            '程序设计语言基础知识': '程序设计语言',
            '程序编译、解释系统': '程序设计语言',
            '系统分析任务': '信息系统分析',
            '系统分析的步骤': '信息系统分析',
            '结构化分析方法': '信息系统分析',
            '系统说明书': '信息系统分析',
            '系统分析工具(UML、U/C矩阵、数据流程图)': '信息系统分析',
            '系统设计概述': '信息系统设计',
            '结构化设计方法和工具': '信息系统设计',
            '系统总体设计': '信息系统设计',
            '系统详细设计': '信息系统设计',
            '系统设计说明书': '信息系统设计',
            '系统运行': '系统管理综述',
            'IT部门人员管理': '系统管理综述',
            '系统日常操作管理': '系统管理综述',
            '系统用户管理': '系统管理综述',
            '运作管理工具': '系统管理综述',
            '成本管理': '系统管理综述',
            '计费管理': '系统管理综述',
            '系统管理标准简介': '系统管理综述',
            '分布式系统的管理': '系统管理综述',
            '信息系统评价概述': '信息系统评价',
            '信息系统评价项目': '信息系统评价',
            '评价项目的标准': '信息系统评价',
            '系统改进建议': '信息系统评价',
            '故障管理概述': '故障管理',
            '故障管理流程': '故障管理',
            '主要故障处理': '故障管理',
            '问题控制与管理': '故障管理',
            '系统实施概述': '信息系统实施',
            '程序设计方法': '信息系统实施',
            '系统测试': '信息系统实施',
            '系统的试运行和转换': '信息系统实施',
            '人员培训': '信息系统实施',
            '数据结构与算法简介': '数据结构与算法',
            '线性表': '数据结构与算法',
            '栈和队列': '数据结构与算法',
            '数组和广义表': '数据结构与算法',
            '树和二叉树': '数据结构与算法',
            '图': '数据结构与算法',
            '安全性简介': '安全性知识',
            '访问控制和鉴别': '安全性知识',
            '加密': '安全性知识',
            '完整性保障': '安全性知识',
            '可用性保障': '安全性知识',
            '计算机病毒的防治与计算机犯罪的防范': '安全性知识',
            '安全分析': '安全性知识',
            '安全管理': '安全性知识',
            '系统管理的定义': '系统管理规划',
            '系统管理服务': '系统管理规划',
            'IT财务管理': '系统管理规划',
            '制定系统管理计划': '系统管理规划',
            '系统维护概述': '系统维护',
            '制定系统维护计划': '系统维护',
            '维护工作的实施': '系统维护',
            '制定计划': '新系统运行及系统转换',
            '制定系统运行体制': '新系统运行及系统转换',
            '系统转换测试与运行测试': '新系统运行及系统转换',
            '系统转换': '新系统运行及系统转换',
            '开发环境管理': '新系统运行及系统转换',
            '系统配置技术': '系统配置和方法',
            '系统性能': '系统配置和方法',
            '系统可靠性': '系统配置和方法',
            '信息化战略与策略': '信息化与标准化',
            '信息化趋势': '信息化与标准化',
            '企业信息资源管理': '信息化与标准化',
            '标准化基础': '信息化与标准化',
            '标准化应用': '信息化与标准化',
            '多媒体技术概论': '多媒体基础知识',
            '多媒体压缩编码技术': '多媒体基础知识',
            '多媒体技术应用': '多媒体基础知识',
            '用户角度的项目': '系统用户支持',
            '用户支持': '系统用户支持',
            '用户咨询': '系统用户支持',
            '帮助服务台': '系统用户支持',
            '人员培训服务': '系统用户支持',
            '安全管理概述': '安全管理',
            '物理安全措施': '安全管理',
            '技术安全措施': '安全管理',
            '管理安全措施': '安全管理',
            '相关法律法规': '安全管理',
            '安全管理的执行': '安全管理',
        }

        # 处理分类
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = xxxtMorningItem()
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
