# -*- coding: utf-8 -*-
import pymongo

import scrapy

from ebookdemo.items import EbookdemoItem


class EbookspiderSpider(scrapy.Spider):
    name = 'ebookspider'

    allowed_domains = ['www.xs84.me', 'www.xinxs84.com']
    http_header = "http://www.xinxs84.com"
    start_urls = ['http://www.xinxs84.com/quanben/1.html']

    def start_requests(self):
        for index in range(100):
            url = 'http://www.xinxs84.com/quanben/%d.html' % index
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = response.xpath('//div[@id="newscontent"]/div[@class="l"]/ul/li/span[@class="s1"]')

        result_dict = {}
        for label in result:
            book_item = EbookdemoItem()
            keys = label.xpath("./text()").extract()[0]
            if keys in result_dict:
                result_dict[keys] += 1
            else:
                result_dict[keys] = 1
            href = label.xpath("./following::span['s2']/a/@href").extract()[0]
            book_name = label.xpath("./following::span['s2']/a/text()").extract()[0]
            book_dict = {'book_name': book_name, 'book_category': keys}
            if book_item.get('book_list', None) is not None:
                book_item['book_list'].append(book_dict)
            else:
                book_item['book_list'] = [book_dict]

            yield scrapy.Request(href, meta={'item': book_item}, callback=self.book_parse)

        pass

    def book_parse(self, response):
        for chapter in response.xpath("//div[@class='box_con']/div/dl/dd"):
            sub_url = chapter.xpath("./a/@href").extract()[0]
            if sub_url:
                yield scrapy.Request(self.http_header + sub_url, meta=response.meta, callback=self.chapter_parse)

    def chapter_parse(self, response):
        client = pymongo.MongoClient(host='localhost', port=27017)
        ebookdb = client['ebookdb']
        data_item = response.meta['item']

        book_item = data_item['book_list'][-1]
        bookcol = ebookdb[book_item['book_name']]

        chapter_name = response.xpath("//div[@class='bookname']/h1/text()").extract_first()
        chapter_content = ''
        for substr in response.xpath("//div[@id='content']/text()").extract():
            chapter_content += substr
        # book_category = response.xpath("//div[@class='con_top']/a[2]/text()").extract_first()
        # book_name = response.xpath("//div[@class='con_top']/a[3]/text()").extract_first()
        chapter_item = {'chapter_name': chapter_name, 'chapter_content': chapter_content}
        if data_item.get('chapter_list', None) is not None:
            data_item['chapter_list'].append(chapter_name)
        else:
            data_item['chapter_list'] = [chapter_name]

        print(book_item['book_name'] + " chapter_name" + chapter_name)
        bookcol.insert_one(chapter_item)
        client.close()
        pass
