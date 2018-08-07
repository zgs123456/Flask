# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

content=MongoClient()
ret=content["tengxun"]["tt"]


class TengxunPipeline(object):
    def process_item(self, item, spider):
        print(item)
        # ret.insert_one(item)
        return item
