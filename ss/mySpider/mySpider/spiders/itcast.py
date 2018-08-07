# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬去的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始抓取的url地址

    def parse(self, response):
        # ret=response.xpath("//div[@class='tea_con']/div/ul/li//h3/text()").extract()
        # print(ret)
        # 分组
        li_list = response.xpath("//div[@class='tea_con']/div/ul/li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath(".//h3/text()").extract_first()
            item['title'] = li.xpath(".//h4/text()").extract_first()
            item['desc'] = li.xpath(".//p/text()").extract_first()

            # print(item)
            yield item
