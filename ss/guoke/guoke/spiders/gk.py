# -*- coding: utf-8 -*-
import scrapy


class GkSpider(scrapy.Spider):
    name = 'gk'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']

    def parse(self, response):
        tr_list=response.xpath("//ul[@class='ask-list-cp']/li")
        # print(tr_list)
        for tr in tr_list:
            item={}
            item['focus_nums']=tr.xpath(".//p[@class='ask-focus-nums']/span/text()").extract_first()#关注数
            item['answer_nums']=tr.xpath(".//p[@class='ask-answer-nums']/span/text()").extract_first()#回答数
            item['title']=tr.xpath(".//div[@class='ask-list-detials']/h2/a/text()").extract_first()#标题
            item['href']=tr.xpath(".//div[@class='ask-list-detials']/h2/a/@href").extract_first()#url地址
            item['content']=tr.xpath(".//p[@class='ask-list-summary']/text()").extract_first()#文本
            item['tag']=tr.xpath(".//a[@class='tag']/text()").extract_first()#标签
            yield scrapy.Request(
                item['href'],
                callback=self.parse_con,
                meta={'item':item}
            )

        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()#获取下一页地址
        if next_url is not None:#判断下一页是否为空
            yield response.follow(next_url, callback=self.parse)#用follow方法拼接地址

    def parse_con(self, response):
        item=response.meta['item']
        div_list=response.xpath("//div[contains(@class,'answer gclear')]")#分组
        answer_list=[]
        for div in div_list:
            cont={ }
            cont['user']=div.xpath(".//a[@class='answer-usr-name']/@title").extract_first()
            cont['answer-date']=div.xpath(".//a[@class='answer-date']/text()").extract_first()
            cont["support_num"] = div.xpath(".//a[@class='answer-digg-up']/span/text()").extract_first()
            cont["content"] = div.xpath(".//div[@class='answer-txt answerTxt gbbcode-content']//text()").extract()
            answer_list.append(cont)
        item['answer_list']=answer_list
        # print(item)
        yield item