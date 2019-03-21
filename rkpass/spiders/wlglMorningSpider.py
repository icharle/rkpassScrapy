# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import wlglMorningItem

# 网络管理员上午题
class WlglmorningspiderSpider(scrapy.Spider):
    name = 'wlglMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['609','566', '531', '494', '475', '437', '383', '360', '247', '246', '244', '242', '240', '238', '236', '234', '232', '230', '228', '226']  # 试卷的所有ID
    field_list = ['20182','20181','20172','20171','20162','20161','20152','20151','20142','20141','20132','20131','20122','20121','20112','20111','20102','20101','20092','20091']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/16_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '网络传输介质': '局域网技术',
            '网络设备': '局域网技术',
            '综合布线技术': '局域网技术',
            '以太网技术': '局域网技术',
            '无线局域网': '局域网技术',
            '虚拟局域网': '局域网技术',
            '网络设计': '局域网技术',
            'OSI参考模型': '网络体系结构',
            '协议层次关系': '网络体系结构',
            'TCP与UDP': '网络体系结构',
            'IP协议': '网络体系结构',
            '低层协议': '网络体系结构',
            '应用层协议': '网络体系结构',
            '网络管理体系': '网络管理技术',
            'Windows基本管理': '网络管理技术',
            'Linux基本管理': '网络管理技术',
            '网络基本参数配置': '网络管理技术',
            '网络管理协议': '网络管理技术',
            '网络诊断命令与故障分析': '网络管理技术',
            '管理工具与网络存储': '网络管理技术',
            'Windows基本操作': '计算机应用知识',
            'Word基本操作': '计算机应用知识',
            'Excel基本操作': '计算机应用知识',
            '上网基础操作': '计算机应用知识',
            '电子政务与电子商务': '计算机应用知识',
            '信息处理实务': '计算机应用知识',
            '云计算': '计算机应用知识',
            '前沿技术': '计算机应用知识',
            '专业英语': '专业英语',
            '网页制作工具选用': '网络编程技术',
            'HTML基础知识': '网络编程技术',
            '动态编程技术': '网络编程技术',
            'XML可扩展标记': '网络编程技术',
            'IP地址分类': '因特网与网络互联技术',
            'IP分配与子网划分': '因特网与网络互联技术',
            'CIDR': '因特网与网络互联技术',
            'TCP/IP端口': '因特网与网络互联技术',
            'IPv6协议': '因特网与网络互联技术',
            '互联网应用': '因特网与网络互联技术',
            '计算机组成': '计算机硬件基础',
            '指令系统': '计算机硬件基础',
            '存储体系': '计算机硬件基础',
            '中断系统': '计算机硬件基础',
            '性能评估': '计算机硬件基础',
            '中央处理器CPU': '计算机硬件基础',
            '信道特性': '数据通信基础',
            '数字编码与编码效率': '数据通信基础',
            '调制技术': '数据通信基础',
            '复用技术': '数据通信基础',
            '差错控制': '数据通信基础',
            '数据交换技术': '数据通信基础',
            'IIS服务配置': '网络应用配置',
            'DNS服务': '网络应用配置',
            'DHCP服务': '网络应用配置',
            'Samba服务': '网络应用配置',
            '代理服务器': '网络应用配置',
            '数制及其转换': '计算机科学基础',
            '数据的表示': '计算机科学基础',
            '数据运算': '计算机科学基础',
            '多媒体技术': '计算机科学基础',
            '操作系统基础': '计算机软件基础',
            '数据库系统基础': '计算机软件基础',
            '程序语言基础': '计算机软件基础',
            '面向对象方法': '计算机软件基础',
            '数据结构': '计算机软件基础',
            '软件工程和项目管理': '计算机软件基础',
            '网络安全基础': '网络安全技术',
            '计算机病毒与网络攻击': '网络安全技术',
            '加密与密钥管理技术': '网络安全技术',
            '数字签名与数字证书': '网络安全技术',
            '入侵检测技术': '网络安全技术',
            '防火墙技术': '网络安全技术',
            '电子商务安全': '网络安全技术',
            '常见广域网技术': '广域网与接入网技术',
            'Internet接入与接口层协议': '广域网与接入网技术',
            'FTTx+LAN接入': '广域网与接入网技术',
            '电话线路接入': '广域网与接入网技术',
            '无线接入': '广域网与接入网技术',
            '交换技术': '广域网与接入网技术',
            '路由技术与路由协议': '广域网与接入网技术',
            '同轴＋光纤接入': '广域网与接入网技术',
            '专利法': '知识产权知识',
            '著作权法': '知识产权知识',
            '计算机软件保护条例': '知识产权知识',
            '反不正当竞争法': '知识产权知识',
            '商标法及实施条例': '知识产权知识',
            '标准化法': '标准化知识',
            'ISO 9000标准族': '标准化知识',
            '应用数学': '应用数学',
        }
        # 处理分类
        # 特殊情况 题目上即为一级分类(该题库无知识点分类)
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = wlglMorningItem()
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
