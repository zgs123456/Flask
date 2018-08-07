# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class SsSpider(scrapy.Spider):
    name = 'ss'
    allowed_domains = ['snbook.suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        div_list = response.xpath("//h3[@class='title2']")
        for div in div_list:
            item = {}
            # 大分类的名称iv
            item["b_cate"] = div.xpath("./a/text()").extract_first()
            m_list=div.xpath("./following-sibling::ul[1]/li")
            for m in m_list:
                item["m_cate"] = m.xpath("./div[@class='second-sort']/a/text()").extract_first()
                s_list = m.xpath("./div[@class='three-sort']/a")
                for s in s_list:
                    item["s_cate"] = s.xpath("./text()").extract_first()
                    item["s_href"] = s.xpath("./@href").extract_first()
                    print(item)

                    yield response.follow(
                        item['s_href'],
                        callback=self.parse_book_list,
                        meta={'item': deepcopy(item)},
                    )
    def parse_book_list(self,response):
        pass