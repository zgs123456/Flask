# -*- coding: utf-8 -*-
import scrapy


class GpSpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['stockapp.finance.qq.com/mstats/']
    start_urls = ['http://stockapp.finance.qq.com/mstats/#mod=list&id=bd012015&module=SS&type=pt012015&sort=32&page=1&max=80']

    def parse(self, response):
        list=response.xpath('//div[@class="navi-brother-title"]/text()')
        print(list)

