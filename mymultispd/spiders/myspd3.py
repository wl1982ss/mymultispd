# -*- coding: utf-8 -*-
import scrapy
from mymultispd.items import MymultispdItem

class Myspd3Spider(scrapy.Spider):
    name = 'myspd3'
    #allowed_domains = ['sina.com.cn']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        item = MymultispdItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(" 以下将显示爬取的网址的标题")
        print(item["urlname"])
