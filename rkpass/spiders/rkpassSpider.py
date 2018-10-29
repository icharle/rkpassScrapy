# -*- coding: utf-8 -*-
import scrapy
import re


class RkpassspiderSpider(scrapy.Spider):
    name = 'rkpassSpider'
    allowed_domains = ['http://www.rkpass.cn/']
    start_urls = []

    for i in range(23, 24):
        start_urls.append('http://www.rkpass.cn/tk_timu/6_553_' + str(i) + '_xuanze.html')

    def parse(self, response):
        data = response.xpath(".//td/span[@class='shisi_text']//text()").extract()  # 爬取题目及选项答案
        dataimg = response.xpath(".//span[@class='shisi_text']/img[last()]/@src").extract()  # 爬取题目及选项中图片
        product_id = re.findall('\((.*?)\)', response.xpath(".//script//text()").extract()[0])[0].split(',')[0].strip(
            "'")  # 该题目id 用于整理答案
        question = "".join(data[0:len(data) - 4])  # 题目
        A = "".join(data[len(data) - 4].split())  # A选项
        B = "".join(data[len(data) - 3].split())  # B选项
        C = "".join(data[len(data) - 2].split())  # C选项
        D = "".join(data[len(data) - 1].split())  # D选项

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

        print(questionImg)
