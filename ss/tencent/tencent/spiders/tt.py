# -*- coding: utf-8 -*-
import urllib.parse
# from tencent.items import TencentItem
import scrapy


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=&tid=0&start=0#a']

    def parse(self, response):
        #分组
        tr_list=response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item={}
            item['position_name']=tr.xpath("./td[1]/a/text()").extract_first()
            item['position_herf']=tr.xpath("./td[1]/a/@herf").extract_first()
            item['position_cate']=tr.xpath("./td[2]/text()").extract_first()
            item['need_num']=tr.xpath("./td[3]/text()").extract_first()
            item['location']=tr.xpath("./td[4]/text()").extract_first()
            item['publish_data']=tr.xpath("./td[5]/text()").extract_first()
            # print(item)
            yield item
            #请求下一页
            next_url=response.xpath("//a[@id='next']/@href").extract_first()
            if next_url !="javascript:;":#判断是否有最后一页
                # next_url="https://hr.tencent.com/"+next_url
                #通过urllie来进行拼接
                # next_url=urllib.parse.urljoin(response.url,next_url)
                # yield scrapy.Request(
                #     next_url,
                #     callback=self.parse
                # )
                #根据response的url对地址进行拼接
                yield response.follow(next_url,callback=self.parse)


