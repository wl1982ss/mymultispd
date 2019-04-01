# -*- coding: utf-8 -*-
import scrapy
from mymultispd.items import MymultispdItem

class Myspd2Spider(scrapy.Spider):
    name = 'myspd2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://www.163.com/']

    def parse(self, response):
        item = MymultispdItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(" 以下将显示爬取的网址的标题")
        print(item["urlname"])
