# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import wlMorningItem


# 网络工程师上午题
class WlmorningspiderSpider(scrapy.Spider):
    name = 'wlMorningSpider'
    allowed_domains = ['www.rkpass.com']
    start_urls = []
    paperId_list = ['624', '594', '558', '522', '484', '465', '421', '372', '347', '307', '147', '111', '109', '106',
                    '104', '102', '100',
                    '98', '96', '94', '92']  # 试卷的所有ID
    field_list = ['20191', '20182', '20181', '20172', '20171', '20162', '20161', '20152', '20151', '20142', '20141',
                  '20132', '20131',
                  '20122', '20121', '20112', '20111', '20102', '20101', '20092', '20091']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/7_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '网络互连设备': '网络互连与互联网',
            '广域网互连': '网络互连与互联网',
            'IP协议': '网络互连与互联网',
            'ICMP': '网络互连与互联网',
            'TCP和LIDP': '网络互连与互联网',
            '域名和地址解析': '网络互连与互联网',
            '网关协议': '网络互连与互联网',
            '路由器技术': '网络互连与互联网',
            'IP组播技术': '网络互连与互联网',
            'IP QoS技术': '网络互连与互联网',
            'Internet应用': '网络互连与互联网',
            'UDP': '网络互连与互联网',
            '信道特性': '数据通信基础',
            '传输介质': '数据通信基础',
            '数据编码': '数据通信基础',
            '数字调制技术': '数据通信基础',
            '脉冲编码调制': '数据通信基础',
            '通信方式和交换方式': '数据通信基础',
            '多路复用技术': '数据通信基础',
            '差错控制': '数据通信基础',
            '数据基础': '数据通信基础',
            '交换机基础': '交换机与路由器',
            '交换机的配置': '交换机与路由器',
            '路由器基础': '交换机与路由器',
            '路由器的配置': '交换机与路由器',
            '访问控制列表': '交换机与路由器',
            'Windows Server 2003网络操作系统基础': '网络操作系统与应用服务器配置',
            'Linux操作系统基础': '网络操作系统与应用服务器配置',
            'Windows服务器配置基础': '网络操作系统与应用服务器配置',
            'DNS服务器配置': '网络操作系统与应用服务器配置',
            'DHCP服务器配置': '网络操作系统与应用服务器配置',
            '网络管理基础': '网络管理',
            '常用的网络工具': '网络管理',
            '网络监视和网络管理工具': '网络管理',
            '网络存储技术': '网络管理',
            '专业英语': '专业英语',
            '网络安全的基本概念': '网络安全',
            '信息加密技术': '网络安全',
            '认证技术': '网络安全',
            '虚拟专用网': '网络安全',
            '应用层安全协议': '网络安全',
            '入侵检测技术与防火墙': '网络安全',
            '病毒防护': '网络安全',
            '计算机中数据的表示及运算': '计算机组成与结构',
            '计算机组成和中央处理器': '计算机组成与结构',
            '存储系统': '计算机组成与结构',
            '输入输出系统': '计算机组成与结构',
            '总线系统': '计算机组成与结构',
            '指令系统': '计算机组成与结构',
            '系统可靠性基础': '计算机组成与结构',
            '局域网技术基础': '局域网和城域网',
            'CSMA／CD协议': '局域网和城域网',
            '以太网': '局域网和城域网',
            '交换式以太网和虚拟局域网': '局域网和城域网',
            '局域网互联': '局域网和城域网',
            '城域网': '局域网和城域网',
            '需求分析和设计方法': '系统开发和运行基础知识',
            '项目管理基础知识': '系统开发和运行基础知识',
            '软件的测试与调试': '系统开发和运行基础知识',
            '系统维护': '系统开发和运行基础知识',
            '程序语言基础': '系统开发和运行基础知识',
            '多媒体基础': '系统开发和运行基础知识',
            '标准化': '标准化和知识产权',
            '知识产权': '标准化和知识产权',
            '操作系统的基本概念': '操作系统',
            '处理机管理': '操作系统',
            '存储管理': '操作系统',
            '设备管理': '操作系统',
            '文件管理': '操作系统',
            '作业管理': '操作系统',
            'IPv6': '下一代互联网',
            '移动IP': '下一代互联网',
            '从IPv4向IPv6的过渡': '下一代互联网',
            '下一代互联网的发展': '下一代互联网',
            '结构化布线系统': '网络系统分析与设计',
            '网络系统分析': '网络系统分析与设计',
            '逻辑网络设计': '网络系统分析与设计',
            '网络结构设计': '网络系统分析与设计',
            '网络故障诊断': '网络系统分析与设计',
            '移动通信': '无线通信网',
            '无线局域网': '无线通信网',
            '无线个域网': '无线通信网',
            '无线城域网': '无线通信网',
            '公共交换电话网': '广域通信网',
            'X.25公共数据网': '广域通信网',
            '帧中继网': '广域通信网',
            'ISDN和ATM的基本概念': '广域通信网',
        }

        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = wlMorningItem()
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
