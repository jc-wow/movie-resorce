# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class DoubanmoviecrawlPipeline(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = '******'
        self.dbName = '*******'
        self.charset = 'utf8mb4'
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.passwd,
                                  db=self.dbName,
                                  charset=self.charset
                                  )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO doubanmovie.movieInfo (id, title, rate, url, cover, director, actor, genre, produceArea, language, releaseDate, runtime, otherName, imdb, officialSite, rating_sum, ratings_on_weight, summary, award, shortComment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            if self.cursor.connection:
                print('start to insert into database')
            else:
                print('retry to reconnect')
                self.cursor = self.db.cursor()     
        except:
            self.db.rollback()
        finally:
            self.cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produceArea'], item['language'], item['releaseDate'], item['runtime'], item['otherName'], item['imdb'], item['officialSite'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['shortComment']))
            self.db.commit()
            print('insert done') 
        return item  

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

