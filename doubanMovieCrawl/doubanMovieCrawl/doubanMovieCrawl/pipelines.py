# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DoubanmoviecrawlPipeline(object):
    def __init__(self):
        self.host = ''
        self.port = ''
        self.user = ''
        self.passwd = ''
        self.dbName = ''
        self.charset = ''
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.passwd,
                                  db=self.dbName,
                                  charset=self.charset
                                  )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = ''
        try:
            if self.cursor.connection:
                print("connection exit")
                self.cursor.execute(sql)
                self.db.commit()
                self.db.close()
            else:
                print('trying to reconnect')
                self.db = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.passwd,
                                          db=self.dbName,
                                          charset=self.charset)
                self.cursor = self.db.cursor()
        except:
            self.db.rollback()
        return item

    def openDatabase(self, spider):
        pass

    def close_spider(self, spider):
        self.db.close()