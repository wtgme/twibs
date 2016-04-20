# -*- coding: utf-8 -*-
"""
Created on 14:57, 14/01/16

@author: wt
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy
from .. import items
from scrapy.http import Request
from scrapy.exceptions import CloseSpider

class twibs_spider(scrapy.Spider):
    name = 'twibs'
    allowed_domains = ["twibs.com"]
    start_urls = [
        "http://www.twibs.com/largest.php"
    ]
    # rules = (
    #     Rule(SgmlLinkExtractor(allow=(''), restrict_xpaths=('//*[@id="l_page"]/div[3]/ul/li[3]/a/@href',)),
    #          callback="parse_dir_contents", follow=True),
    # )
    # def parse(self, response):
    #     for href in response.xpath('//*[@id="l_page"]/div[3]/ul/li[3]/a/@href'):
    #         url = response.urljoin(href.extract())
    #         print
    #         print href.extract()
    #         print '----------------', url
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)
    # def parse_start_url(self, response):
    #     return self.parse_dir_contents(response)

    # def parse_category(self, response):
    #     //*[@id="l_page"]/div[2]/div[2]/h4
    #     //*[@id="l_page"]/div[2]/div[18]
    #     //*[@id="l_page"]/div[2]/li[14]
    #     //*[@id="l_page"]/div[2]/li[15]
    #     //*[@id="l_page"]/div[2]/li[29]


    def parse(self, response):
        infor = response.xpath('//*[@id="l_page"]/div[2]/div')
        if len(infor) == 0:
            raise CloseSpider('---------------------End Search!---------------')

        for com in infor[1:]:
            item = items.TwibsItem()
            item['name'] = com.xpath('div[2]/a/text()').extract()
            item['add'] = com.xpath('div[2]/text()').extract()
            item['bio'] = com.xpath('div[2]/div[1]/text()').extract()
            tags = []
            for tag in com.xpath('div[2]/div[2]/span[2]/li'):
                tag = tag.xpath('a/text()').extract()
                tags.append(tag)
            item['tags'] = tags
            yield item

        nexthref = response.xpath('//*[@id="l_page"]/div[3]/ul/li[3]/a/@href')[0]
        url = response.urljoin(nexthref.extract())
        if url:
            yield Request(url, callback=self.parse)

