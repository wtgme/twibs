# -*- coding: utf-8 -*-
"""
Created on 14:57, 14/01/16

@author: wt
"""
import scrapy
from .. import items
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
from scrapy.selector import HtmlXPathSelector

class medical(scrapy.Spider):
    name = 'icnarc'
    allowed_domains = ["icnarc.org"]
    start_urls = [
        'https://www.icnarc.org/Modules/ICM/1'
        # 'https://www.icnarc.org/Modules/ICM/2'
    ]

    def parse(self, response):
        infor = response.xpath('//*[@id="ICMBody"]/ul')
        if len(infor) == 0:
            raise CloseSpider('---------------------End Search!---------------')

        for com in infor:
            nexthref = com.xpath('a/@href')[0]
            url = response.urljoin(nexthref.extract())
            if url:
                yield Request(url, callback=self.parse_1)


    def parse_1(self, response):




