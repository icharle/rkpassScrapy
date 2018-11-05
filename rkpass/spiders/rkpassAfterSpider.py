# -*- coding: utf-8 -*-
import scrapy
import re
from rkpass.items import rkpassAfterItem


class RkpassafterspiderSpider(scrapy.Spider):
    name = 'rkpassAfterSpider'
    allowed_domains = ['www.rkpass.com']
    start_urls = []

    for i in range(1, 7):
        start_urls.append('http://www.rkpass.cn/tk_timu/6_431_' + str(i) + '_anli.html')

    def parse(self, response):
        questionImg = response.xpath(".//span[@class='shisi_text']/img/@src").extract()  # 爬取题目中图片
        product_id = re.findall('\((.*?)\)', response.xpath(".//script//text()").extract()[0])[0].split(',')[0].strip(
            "'")  # 该题目id 用于整理答案
        tihao = re.findall('↓第(.*?)题', "".join(response.xpath(".//span[@class='hui']//text()").extract()))  # 题号
        question = "".join(response.xpath(".//table/tr[2]/td/span[@class='shisi_text']//text()").extract())  # 题目

        optionA = "".join("".join(response.xpath(".//table/tr[4]/td/text()").extract()).split())  # tr[] 4,6,8,10
        optionB = "".join("".join(response.xpath(".//table/tr[6]/td/text()").extract()).split())  # tr[] 4,6,8,10
        optionC = "".join("".join(response.xpath(".//table/tr[8]/td/text()").extract()).split())  # tr[] 4,6,8,10
        optionD = "".join("".join(response.xpath(".//table/tr[10]/td/text()").extract()).split())  # tr[] 4,6,8,10
        optionE = "".join("".join(response.xpath(".//table/tr[12]/td/text()").extract()).split())  # tr[] 4,6,8,10

        # 收集数据
        item = rkpassAfterItem()
        item['question'] = question
        item['questionImg'] = questionImg
        item['optionA'] = optionA
        item['optionB'] = optionB
        item['optionC'] = optionC
        item['optionD'] = optionD
        item['optionE'] = optionE

        url = 'http://www.rkpass.cn/tk_jiexi.jsp?product_id=' + product_id + '&tixing=anli&answer=&paper_id=431&tihao=' + "".join(
            tihao) + '&cache=false'
        yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']  # 接收上级已爬取的数据
        optionAanswer = ''
        optionAanswerImg = ''
        optionBanswer = ''
        optionBanswerImg = ''
        optionCanswer = ''
        optionCanswerImg = ''
        optionDanswer = ''
        optionDanswerImg = ''
        optionEanswer = ''
        optionEanswerImg = ''
        data = "".join(response.xpath(".//table/tr/td/table/tr/td").extract())
        dataInfo = data.split('软考在线[rkpass.cn]答案解析：')
        for i in range(1, len(dataInfo)):
            if i == 1:
                optionAanswer = "".join(re.sub('</?\w+[^>]*>', '', dataInfo[i])).strip()  # 答案中的文字
                optionAanswerImg = "".join(re.findall('src="(.*?)"', dataInfo[i]))  # 答案中的图片
            elif i == 2:
                optionBanswer = re.sub('</?\w+[^>]*>', '', dataInfo[i])  # 答案中的文字
                optionBanswerImg = "".join(re.findall('src="(.*?)"', dataInfo[i]))  # 答案中的图片
            elif i == 3:
                optionCanswer = re.sub('</?\w+[^>]*>', '', dataInfo[i])  # 答案中的文字
                optionCanswerImg = "".join(re.findall('src="(.*?)"', dataInfo[i]))  # 答案中的图片
            elif i == 4:
                optionDanswer = re.sub('</?\w+[^>]*>', '', dataInfo[i])  # 答案中的文字
                optionDanswerImg = "".join(re.findall('src="(.*?)"', dataInfo[i]))  # 答案中的图片
            elif i == 5:
                optionEanswer = re.sub('</?\w+[^>]*>', '', dataInfo[i])  # 答案中的文字
                optionEanswerImg = "".join(re.findall('src="(.*?)"', dataInfo[i]))  # 答案中的图片

        # 接收二级答案页面数据
        item['optionAanswer'] = optionAanswer
        item['optionAanswerImg'] = optionAanswerImg
        item['optionBanswer'] = optionBanswer
        item['optionBanswerImg'] = optionBanswerImg
        item['optionCanswer'] = optionCanswer
        item['optionCanswerImg'] = optionCanswerImg
        item['optionDanswer'] = optionDanswer
        item['optionDanswerImg'] = optionDanswerImg
        item['optionEanswer'] = optionEanswer
        item['optionEanswerImg'] = optionEanswerImg
        item['field'] = '20161'

        return item
