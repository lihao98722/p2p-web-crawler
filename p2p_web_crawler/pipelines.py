# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings


class MongoDBPipeline(object):
    __Maximum = settings['NUMBER_OF_ITEMS_TO_WRITE']

    def __init__(self):
        self.items = []
        client = MongoClient(host=settings['MONGODB_SERVER'], port=settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.coll = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        self.items.append(dict(item))
        # insert data when the number of crawled web pages reach certain amount.
        if len(self.items) >= self.__Maximum:
            self.coll.insert(self.items)
            del self.items[:]

    # insert remaining data before closing this spider
    def close_spider(self, spider):
        if len(self.items) > 0:
            self.coll.insert(self.items)
            del self.items[:]