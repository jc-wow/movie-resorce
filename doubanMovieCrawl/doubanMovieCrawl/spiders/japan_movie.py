import settings
import scrapy
from parse import Parse


class JapanMovie(scrapy.Spider):
	name = 'chinieseMovie'
	allowed_domains = ['douban.com']
	custom_settings = {
		'ITEM_PIPELINES': {
			'pipelines.JapanMovie': 401
		},
		'DOWNLOADER_MIDDLEWARES': {
			'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
			'middlewares.RandomUserAgentMiddleware': 310,
			'middlewares.RandomProxyMiddleware': 350,
			'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 380
		},
		'CONCURRENT_REQUESTS': 100,
		'DOWNLOAD_DELAY': 3,
		'DOWNLOAD_TIMEOUT': 5
	}

	def __init__(self, name=None, **kwargs):
		super().__init__(name=name, **kwargs)
		self.headers = settings.Headers
		self.Parse = Parse()

	def start_requests(self):
		startPage = '0'
		doubanMovieURL = settings.MovieURL['japanMovie']
		yield scrapy.Request(doubanMovieURL + startPage, callback=self.Parse.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]})

	def errback_httpbin(self, failure):
		self.logger.error(repr(failure))
