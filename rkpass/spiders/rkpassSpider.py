# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re


class RkpassspiderSpider(scrapy.Spider):
    name = 'rkpassSpider'
    allowed_domains = ['http://www.rkpass.cn/']
    start_urls = []

    for i in range(36, 37):
        start_urls.append('http://www.rkpass.cn/tk_timu/6_553_' + str(i) + '_xuanze.html')

    def parse(self, response):
        bsObj = BeautifulSoup(response.text)
        pictures = bsObj.findAll('img', {'src': re.compile('.*\/.*\/.*\/.*\/.*\.png')})
        titles = bsObj.find_all('span', {'class': 'shisi_text'})
        for txt in titles:
            txt = txt.text
            txt = re.sub('\s*', '', txt)
            print(txt)

        for picture in pictures:
            url = re.compile('http\:\/\/www\.rkpass\.cn\/ruankao\_work\_version\_0103\/userfile\/image\/(.*)')
            res = url.search(picture['src']).groups()[0]
            print(res)