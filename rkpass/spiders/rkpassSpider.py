# -*- coding: utf-8 -*-
import scrapy


class RkpassspiderSpider(scrapy.Spider):
    name = 'rkpassSpider'
    allowed_domains = ['http://www.rkpass.cn/']
    start_urls = []

    def parse(self, response):
        pass
