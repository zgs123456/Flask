# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

content=MongoClient()
ret=content["gk"]["gk"]
class GuokePipeline(object):
    def process_item(self, item, spider):
        ret.insert_one(item)
        print(item)
        return item
