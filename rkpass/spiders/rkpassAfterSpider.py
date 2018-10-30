# -*- coding: utf-8 -*-
import scrapy
import re


class RkpassafterspiderSpider(scrapy.Spider):
    name = 'rkpassAfterSpider'
    allowed_domains = ['www.rkpass.com']
    start_urls = []

    for i in range(2, 3):
        start_urls.append('http://www.rkpass.cn/tk_timu/6_580_' + str(i) + '_anli.html')

    def parse(self, response):
        dataimg = response.xpath(".//span[@class='shisi_text']/img/@src").extract()  # 爬取题目中图片
        product_id = re.findall('\((.*?)\)', response.xpath(".//script//text()").extract()[0])[0].split(',')[0].strip(
            "'")  # 该题目id 用于整理答案
        question = "".join(response.xpath(".//table/tr[2]/td/span[@class='shisi_text']//text()").extract())  # 题目

        wenti = "".join(response.xpath(".//table/tr/td/text()").extract()) # tr[] 4,6,8,10

        print(wenti)
