# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwibsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    add = scrapy.Field()
    bio = scrapy.Field()
    tags = scrapy.Field()


class MedicalItem(scrapy.Item):
    icmcode = scrapy.Field()
    name = scrapy.Field()
