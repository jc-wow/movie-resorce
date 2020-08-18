# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import logging
from DBUtils.PooledDB import PooledDB
import json


class Pool(object):
	__pool = None
	config = {
		'host': 'localhost',
		'port': 3306,
		'user': 'root',
		'passwd': 'wangchi6992830',
		'dbName': 'doubanmovie',
		'charset': 'utf8mb4'
	}

	@staticmethod
	def get_conn():
		if not Pool.__pool:
			__pool = PooledDB(
				creator=pymysql,
				mincached=1,
				maxcached=20,
				host=Pool.config['host'],
				port=Pool.config['port'],
				db=Pool.config['dbName'],
				user=Pool.config['user'],
				passwd=Pool.config['passwd'],
				charset=Pool.config['charset']
			)
			return __pool.connection()


class HighScoreMovie(Pool):

	def __init__(self):
		self.__conn = Pool.get_conn()
		self.__cursor = self.__conn.cursor()

	def process_item(self, item, spider):
		insert_data_sql = 'INSERT INTO doubanmovie.high_score_movies (id, title, rate, url, cover, director, actor, genre, produce_area, language, release_date, runtime, other_name, imdb, official_site, rating_sum, ratings_on_weight, summary, award, short_comment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		try:
			self.insert(item, insert_data_sql)
		except Exception as e:
			logging.error(e)

	def insert(self, item, sql):
		try:
			if self.__cursor:
				self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produce_area'], item['language'], item['release_date'], item['runtime'],
											item['other_name'], item['imdb'], item['official_site'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['short_comment'], item['original_photo'], json.dumps(item['similar_like']), item['tag'], item['ost']))
				self.__conn.commit()
				print('insert done')
		except Exception as e:
			logging.error(e)


class ChinieseMovie(Pool):
	
	def __init__(self):
		self.__conn = Pool.get_conn()
		self.__cursor = self.__conn.cursor()

	def process_item(self, item, spider):
		insert_data_sql = 'INSERT INTO doubanmovie.chiniese_movies (id, title, rate, url, cover, director, actor, genre, produce_area, language, release_date, runtime, other_name, imdb, official_site, rating_sum, ratings_on_weight, summary, award, short_comment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		try:
			self.insert(item, insert_data_sql)
		except Exception as e:
			logging.error(e)

	def insert(self, item, sql):
		try:
			if self.__cursor:
				self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produce_area'], item['language'], item['release_date'], item['runtime'],
											item['other_name'], item['imdb'], item['official_site'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['short_comment'], item['original_photo'], json.dumps(item['similar_like']), item['tag'], item['ost']))
				self.__conn.commit()
				print('insert done')
		except Exception as e:
			logging.error(e)


class EuropeMovie(Pool):
	
	def __init__(self):
		self.__conn = Pool.get_conn()
		self.__cursor = self.__conn.cursor()

	def process_item(self, item, spider):
		insert_data_sql = 'INSERT INTO doubanmovie.europe_movies (id, title, rate, url, cover, director, actor, genre, produce_area, language, release_date, runtime, other_name, imdb, official_site, rating_sum, ratings_on_weight, summary, award, short_comment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		try:
			self.insert(item, insert_data_sql)
		except Exception as e:
			logging.error(e)

	def insert(self, item, sql):
		try:
			if self.__cursor:
				self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produce_area'], item['language'], item['release_date'], item['runtime'],
											item['other_name'], item['imdb'], item['official_site'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['short_comment'], item['original_photo'], json.dumps(item['similar_like']), item['tag'], item['ost']))
				self.__conn.commit()
				print('insert done')
		except Exception as e:
			logging.error(e)


class KoreaMovie(Pool):
	
	def __init__(self):
		self.__conn = Pool.get_conn()
		self.__cursor = self.__conn.cursor()

	def process_item(self, item, spider):
		insert_data_sql = 'INSERT INTO doubanmovie.korea_movies (id, title, rate, url, cover, director, actor, genre, produce_area, language, release_date, runtime, other_name, imdb, official_site, rating_sum, ratings_on_weight, summary, award, short_comment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		try:
			self.insert(item, insert_data_sql)
		except Exception as e:
			logging.error(e)

	def insert(self, item, sql):
		try:
			if self.__cursor:
				self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produce_area'], item['language'], item['release_date'], item['runtime'],
											item['other_name'], item['imdb'], item['official_site'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['short_comment'], item['original_photo'], json.dumps(item['similar_like']), item['tag'], item['ost']))
				self.__conn.commit()
				print('insert done')
		except Exception as e:
			logging.error(e)


class JapanMovie(Pool):
	
	def __init__(self):
		self.__conn = Pool.get_conn()
		self.__cursor = self.__conn.cursor()

	def process_item(self, item, spider):
		insert_data_sql = 'INSERT INTO doubanmovie.japan_movies (id, title, rate, url, cover, director, actor, genre, produce_area, language, release_date, runtime, other_name, imdb, official_site, rating_sum, ratings_on_weight, summary, award, short_comment, original_photo, similar_like, tag, ost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		try:
			self.insert(item, insert_data_sql)
		except Exception as e:
			logging.error(e)

	def insert(self, item, sql):
		try:
			if self.__cursor:
				self.__cursor.execute(sql, (item['id'], item['title'], item['rate'], item['url'], item['cover'], item['director'], item['actor'], item['genre'], item['produce_area'], item['language'], item['release_date'], item['runtime'],
											item['other_name'], item['imdb'], item['official_site'], item['rating_sum'], item['ratings_on_weight'], item['summary'], item['award'], item['short_comment'], item['original_photo'], json.dumps(item['similar_like']), item['tag'], item['ost']))
				self.__conn.commit()
				print('insert done')
		except Exception as e:
			logging.error(e)

