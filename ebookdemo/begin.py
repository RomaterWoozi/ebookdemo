# -*- coding: utf-8 -*-
import pymongo

from scrapy import cmdline

if __name__ == '__main__':
    # drop清除库
    client = pymongo.MongoClient(host='localhost', port=27017)
    dblist = client.list_database_names()
    if 'ebookdb' in dblist:
        client.drop_database('ebookdb')
    client.close()

    cmdline.execute("scrapy crawl ebookspider -o data.json".split())
