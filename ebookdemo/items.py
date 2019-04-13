# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbookdemoItem(scrapy.Item):
    # define the fields for your item here like:
    data_list = scrapy.Field()
    book_category = scrapy.Field()
    book_list = scrapy.Field()
    book_name = scrapy.Field()
    chapter_list = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_content = scrapy.Field()
    pass
