# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import mediaMorningItem

# 多媒体应用设计师上午题
class MediamorningspiderSpider(scrapy.Spider):
    name = 'mediaMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['586', '517', '447', '256', '254', '252', '250', '248']  # 试卷的所有ID
    field_list = ['20171', '20161', '20151', '20141', '20131', '20121', '20111', '20101']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/11_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '视频信息获取和处理': '多媒体数据处理技术',
            '音频信息获取和处理': '多媒体数据处理技术',
            '多媒体数据压缩编码技术基础': '多媒体数据处理技术',
            '图像信息获取和处理': '多媒体数据处理技术',
            '多媒体的定义和关键技术': '多媒体技术及其应用',
            '多媒体计算机系统结构': '多媒体技术及其应用',
            '多媒体传输协议': '多媒体技术及其应用',
            '多媒体技术的应用': '多媒体技术及其应用',
            '多媒体技术的发展趋势': '多媒体技术及其应用',
            '多媒体技术基础': '多媒体技术及其应用',
            '电视': '多媒体技术及其应用',
            '多媒体技术标准': '多媒体技术及其应用',
            '多媒体应用软件': '多媒体技术及其应用',
            '印刷和打印': '多媒体技术及其应用',
            '计算机软件的分类及常用软件': '计算机软件基础知识',
            '操作系统的原理及使用': '计算机软件基础知识',
            '程序设计语言基础知识': '计算机软件基础知识',
            '软件工程': '计算机软件基础知识',
            '软件项目管理': '计算机软件基础知识',
            '网络参考模型与网络协议': '计算机网络与通信基础知识',
            '局域网、广域网基本概念及其功能': '计算机网络与通信基础知识',
            'Internet的基本概念及其应用': '计算机网络与通信基础知识',
            '宽带网络及其接入技术': '计算机网络与通信基础知识',
            '无线通信技术': '计算机网络与通信基础知识',
            '网络设备': '计算机网络与通信基础知识',
            '网络基础': '计算机网络与通信基础知识',
            '综合布线': '计算机网络与通信基础知识',
            '专业英语': '专业英语',
            '计算机的基础组成原理': '计算机硬件及系统组成',
            '中央处理器CPU': '计算机硬件及系统组成',
            '内部和外部存储器': '计算机硬件及系统组成',
            '输入输出接口及其设备': '计算机硬件及系统组成',
            '显示器': '计算机硬件及系统组成',
            '知识产权': '知识产权的有关法律、法规',
            '计算机软件著作权': '知识产权的有关法律、法规',
            '商标权': '知识产权的有关法律、法规',
            '计算机技术概述': '计算机基础知识',
            '数字技术基础': '计算机基础知识',
            '计算机中数据的表示': '计算机基础知识',
            '数据校验码': '计算机基础知识',
            '信息安全性基本概念': '信息安全性知识',
            '计算机病毒防范': '信息安全性知识',
            '入侵检测与防范措施': '信息安全性知识',
            '加密解密机制与信息加密策略': '信息安全性知识',
            '身份验证和访问控制策略': '信息安全性知识',
            '国际标准、国家标准、行业标准、企业标准': '标准化知识',
            '编码标准、多媒体有关的技术标准': '标准化知识',
            '标准化机构': '标准化知识',
            '信息化基本概念': '信息化基本知识',
            '国民经济与社会信息化战略': '信息化基本知识',
            '有关信息化的其他概念': '信息化基本知识'
        }

        # 处理分类
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = mediaMorningItem()
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