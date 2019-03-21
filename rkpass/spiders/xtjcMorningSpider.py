# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import xtjcMorningItem

# 系统集成项目管理工程师上午题
class XtjcmorningspiderSpider(scrapy.Spider):
    name = 'xtjcMorningSpider'
    allowed_domains = ['www.rkpass.cn']
    start_urls = []
    paperId_list = ['597', '556', '520', '492', '461', '413', '376', '342', '309', '308', '70', '67', '65', '63', '61', '59',
                    '57', '55', '53', '51']  # 试卷的所有ID
    field_list = ['20182', '20181', '20172', '20171', '20162', '20161', '20152', '20151', '20142', '20141', '20132', '20131',
                  '20122', '20121', '20112', '20111', '20102', '20101', '20092', '20091']  # 跟上行试卷所有ID对应考试场次

    for j in range(len(paperId_list)):
        for i in range(1, 76):
            start_urls.append(
                'http://www.rkpass.cn/tk_timu/2_' + str(paperId_list[j]) + '_' + str(i) + '_xuanze.html?field=' +
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
            '系统集成': '信息系统集成专业技术知识',
            '信息系统建设': '信息系统集成专业技术知识',
            '软件工程': '信息系统集成专业技术知识',
            '面向对象系统分析与设计': '信息系统集成专业技术知识',
            '软件体系结构': '信息系统集成专业技术知识',
            '典型应用集成技术': '信息系统集成专业技术知识',
            '计算机网络知识': '信息系统集成专业技术知识',
            '新一代信息技术的发展': '新技术的发展',
            '专业英语': '专业英语',
            '立项管理内容': '立项管理',
            '建设方的立项管理': '立项管理',
            '承建方的立项管理': '立项管理',
            '签订合同': '立项管理',
            '项目整体管理的含义、主要活动和流程': '项目整体管理',
            '项目章程': '项目整体管理',
            '编制初步范围说明书': '项目整体管理',
            '项目管理计划': '项目整体管理',
            '项目计划实施的监督和控制': '项目整体管理',
            '项目整体变更控制': '项目整体管理',
            '项目收尾': '项目整体管理',
            '活动定义': '项目进度管理',
            '活动排序': '项目进度管理',
            '活动资源估算': '项目进度管理',
            '活动历时估算': '项目进度管理',
            '制定进度计划': '项目进度管理',
            '项目进度控制': '项目进度管理',
            '信息化概念': '信息化基础',
            '电子政务': '信息化基础',
            '企业信息化与电子政务': '信息化基础',
            '信息资源开发利用及共享': '信息化基础',
            '信息化法规政策标准规范': '信息化基础',
            '项目管理的理论基础与体系': '项目管理一般知识',
            '项目生命周期和组织': '项目管理一般知识',
            '风险和风险管理': '项目风险管理',
            '制定风险管理计划': '项目风险管理',
            '风险识别': '项目风险管理',
            '制定定性风险管理计划': '项目风险管理',
            '定量风险分析': '项目风险管理',
            '应对风险的基本措施（规避/接受/减轻/转移）': '项目风险管理',
            '风险监控': '项目风险管理',
            '质量管理基础': '项目质量管理',
            '制定项目质量计划': '项目质量管理',
            '项目质量保证': '项目质量管理',
            '项目质量控制': '项目质量管理',
            '项目沟通管理的基本概念': '项目沟通管理',
            '沟通管理计划编制': '项目沟通管理',
            '信息分发': '项目沟通管理',
            '绩效报告': '项目沟通管理',
            '项目干系人管理': '项目沟通管理',
            '采购管理的相关概念和主要过程': '项目采购管理',
            '编制采购计划': '项目采购管理',
            '编制询价计划': '项目采购管理',
            '询价': '项目采购管理',
            '招标': '项目采购管理',
            '合同管理及收尾': '项目采购管理',
            '信息系统项目相关信息（文档）及其管理': '信息（文档）与配置管理',
            '配置管理': '信息（文档）与配置管理',
            '项目变更基本概念': '项目变更管理',
            '变更管理的基本原则': '项目变更管理',
            '变更管理组织机构与工作程序': '项目变更管理',
            '项目变更管理的工作内容': '项目变更管理',
            '项目成本管理概念及相关术语': '项目成本管理',
            '项目成本估算': '项目成本管理',
            '项目成本预算': '项目成本管理',
            '项目成本控制': '项目成本管理',
            '项目范围和项目范围管理': '范围管理',
            '制定范围计划': '范围管理',
            '范围定义和工作分解结构': '范围管理',
            '项目范围确认': '范围管理',
            '项目范围控制': '范围管理',
            '信息安全管理': '信息安全管理',
            '信息系统安全': '信息安全管理',
            '物理安全管理': '信息安全管理',
            '人员安全管理': '信息安全管理',
            '应用系统安全管理': '信息安全管理',
            '信息系统服务管理': '信息系统项目管理',
            '信息系统集成资质管理': '信息系统项目管理',
            '信息系统工程监理资质管理': '信息系统项目管理',
            '项目合同': '项目合同管理',
            '项目合同的分类': '项目合同管理',
            '项目合同签订': '项目合同管理',
            '项目合同管理': '项目合同管理',
            '项目人力资源管理有关概念': '项目人力资源管理',
            '项目人力资源计划制定': '项目人力资源管理',
            '项目团队组织建设': '项目人力资源管理',
            '项目团队管理': '项目人力资源管理',
            '运维服务管理': '运维服务管理知识',
            '法律': '法律法规和标准规范',
            '软件工程的国家标准': '法律法规和标准规范',
            '机房、网络、综合布线相关标准': '法律法规和标准规范',
            '知识产权管理概念': '知识产权管理',
            '知识产权管理相关法律法规': '知识产权管理',
            '知识产权管理工作的范围和内容': '知识产权管理',
            '项目收尾的内容': '项目收尾管理',
            '对信息系统的后续工作的支持': '项目收尾管理',
            '项目组人员转移': '项目收尾管理',
            '': '',
        }

        # 处理分类
        knowledgeOne = info[knowledgeTwo]  # 知识点一级分类

        # 收集数据
        item = xtjcMorningItem()
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