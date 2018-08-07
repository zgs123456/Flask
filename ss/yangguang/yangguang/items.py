# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()#编号
    title = scrapy.Field()#帖子标签
    href = scrapy.Field()#帖子url
    status = scrapy.Field()#处理状态
    name = scrapy.Field()#用户名
    publish_data= scrapy.Field()#时间
    img = scrapy.Field()#图片
    content = scrapy.Field()#文本内容


