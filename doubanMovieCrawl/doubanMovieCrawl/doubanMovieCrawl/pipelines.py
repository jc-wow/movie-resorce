# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import logging
from DBUtils.PooledDB import PooledDB


class DoubanmoviecrawlPipeline(object):
    __pool = None

    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'wangchi6992830'
        self.dbName = 'doubanmovie'
        self.charset = 'utf8mb4'
        self.__conn = DoubanmoviecrawlPipeline.get_conn()
        self.__cursor = self.__conn.cursor()

    @staticmethod
    def get_conn():
        if not DoubanmoviecrawlPipeline.__pool:
            __pool = PooledDB(
                creator = pymysql,
                mincached = 1,
                maxcached = 20,
                host = self.host,
                port = self.port,
                db = self.dbName,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            return __pool.connection()

    def process_item(self, item, spider):
        insert_data_sql = 'INSERT INTO doubanmovie.high_score_movies (id, title, rate, url, cover, director, actor, genre, produceArea, language, releaseDate, runtime, otherName, imdb, officialSite, rating_sum, ratings_on_weight, summary, award, shortComment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            self.insert(item, insert_data_sql)
        except Exception as e:
            logging.error(e)

    def insert(self, item, sql):
        try:
            self.__cursor:
                print('start to insert into database......')
                movieData = self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produceArea'], item['language'], item['releaseDate'],
                                      item['runtime'], item['otherName'], item['imdb'], item['officialSite'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['shortComment'], item['original_photo'], item['similar_like'], item['tag'], item['ost']))
        except:
            self.db.rollback()
       
