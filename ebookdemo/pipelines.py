# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ebookdemo.spiders.ebookspider import EbookspiderSpider


class EbookdemoPipeline(object):
    curpath = "E:\\tmp"

    # def spider_closed(self, spider):
    #     spider.client.close()

    def process_item(self, item, spider):
        print(item)

        return item
