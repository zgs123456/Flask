# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 获取大的分组
        div_list = response.xpath("//div[@class='menu-list']/div[@class='menu-item']")
        div_sub_list = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
        for div in div_list:
            item = {}
            # 大分类的名称
            item["b_cate"] = div.xpath("//h3/text()").extract_first()
            # 大分类的所以中间分类的位置
            current_sub_list = div_sub_list[div_list.index(div)]
            # 获取中间分类的分组
            p_list = current_sub_list.xpath("//div[@class='submenu-left']/p[@class='submenu-item']")
            for p in p_list:
                # 中间分类的小分类
                item["m_cate"] = p.xpath("./a/text()").extract_first()
                # 获取小分类的分组
                li_list = p.xpath("./following-sibling::ul[1]/li")
                for li in li_list:
                    # 获取小分类名字
                    item["s_cate"] = li.xpath("./a/text()").extract_first()
                    item["s_href"] = li.xpath("./a/@href").extract_first()
                    # print(item)
                    # 请求列表页
                    yield scrapy.Request(
                        item['s_href'],
                        callback=self.parse_book_list,
                        meta={'item': deepcopy(item)}
                    )
                    # 发送请求，获取列表页第一页后一部分的数据
                    next_part_url_temp = "https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp=0&il=0&iy=0&adNumber=0&n=1&ch=4&sesab=ABBAAA&id=IDENTIFYING&cc=010&paging=1&sub=0"
                    # 获取url地址的ci
                    ci = item["s_href"].split("-")[1]
                    next_part_url = next_part_url_temp.format(ci)
                    yield scrapy.Request(
                        next_part_url,
                        callback=self.parse_book_list,
                        meta={"item": deepcopy(item)}
                    )

    def parse_book_list(self, response):
        item = response.meta['item']
        # 获取分组
        li_list = response.xpath("//div[@id='filter-results']/ul/li")
        for li in li_list:
            # 书名
            item["book_name"] = li.xpath(".//p[@class='sell-point']/a/text()").extract_first().strip()
            # url地址
            item["book_href"] = li.xpath(".//p[@class='sell-point']/a/@href").extract_first()
            # 书店地址
            item["book_store_name"] = li.xpath(".//p[contains(@class,'seller oh no-more')]/a/text()").extract_first()
            # print(item)

            # 发送详情页的请求
            yield response.follow(
                item['book_href'],
                callback=self.parse_book_datail,
                meta={'item': deepcopy(item)}
            )
        # 前半部分数据的url地址
        next_url1 = "https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=0&adNumber=0&n=1&ch=4&sesab=ABBAAA&id=IDENTIFYING&cc=010"
        # 后半部分数据的url地址
        next_url2 = "https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=0&adNumber=0&n=1&ch=4&sesab=ABBAAA&id=IDENTIFYING&cc=010&paging=1&sub=0"
        ci = item["s_href"].split("-")[1]
        # 当前页码数
        current_page = re.findall('param.currentPage="(.*?)";', response.body.decode())[0]
        # 总页码数
        total_page = re.findall('param.pageNumber="(.*?)";', response.body.decode())[0]
        if int(current_page) < int(total_page):
            next_page_num = int(current_page) + 1
            # 组织前半部分url
            next_url1 = next_url1.format(ci, next_page_num)
            yield scrapy.Request(
                next_url1,
                callback=self.parse_book_list,
                meta={"item": item}
            )
            # 组织后半部分url
            next_url2 = next_url2.format(ci, next_page_num)
            yield scrapy.Request(
                next_url2,
                callback=self.parse_book_list,
                meta={"item": item}
            )

    def parse_book_datail(self, response):  # 处理详情页
        item = response.meta['item']
        price_temp_url = "https://pas.suning.com/nspcsale_0_000000000{}_000000000{}_{}_10_010_0100101_226503_1000000_9017_10106____{}_{}___.html"
        p1 = response.url.split("/")[-1].split(".")[0]
        p3 = response.url.split("/")[-2]
        p4 = re.findall('"catenIds":"(.*?)",', response.body.decode())
        if len(p4) > 0:
            p4 = p4[0]
            p5 = re.findall('"weight":"(.*?)",', response.body.decode())[0]

            price_url = price_temp_url.format(p1, p1, p3, p4, p5)
            yield scrapy.Request(
                price_url,
                callback=self.parse_book_pirce,
                meta={"item": item}
            )

    def parse_book_pirce(self, response):  # 获取价格
        item = response.meta['item']
        item["book_price"] = re.findall('"netPrice":"(.*?)"', response.body.decode())[0]
        # print(item)
        yield item
