# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanHighestmoviecrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    id = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    genre = scrapy.Field()
    produce_area = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    runtime = scrapy.Field()
    other_name = scrapy.Field()
    imdb = scrapy.Field()
    official_site = scrapy.Field()
    rating_sum = scrapy.Field()
    ratings_on_weight = scrapy.Field()
    summary = scrapy.Field()
    award = scrapy.Field()
    short_comment = scrapy.Field()
    original_photo = scrapy.Field()
    similar_like = scrapy.Field()
    tag = scrapy.Field()
    ost = scrapy.Field()
    
    pass
