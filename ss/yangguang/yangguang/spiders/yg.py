# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        # 提取当前页的数据
        # 分组在提取
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        # 获取下一页
        print(tr_list)
        for tr in tr_list:
            item = YangguangItem()
            item['num'] = tr.xpath("./td[1]/text()").extract_first()
            item['title'] = tr.xpath("./td[2]/a/text()").extract_first()
            item['href'] = tr.xpath("./td[2]/a/text()").extract_first()
            item['status'] = tr.xpath("./td[3]/span/text()").extract_first()
            item['name'] = tr.xpath("./td[4]/text()").extract_first()
            item['publish_data'] = tr.xpath("./td[5]/text()").extract_first()
            print(item)
