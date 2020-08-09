from scrapy.selector import Selector
import json
import re
import items
import settings
from scrapy import FormRequest
import scrapy


class ChinieseMovie(scrapy.Spider):
	name = 'chinieseMovie'
	allowed_domains = ['douban.com']
	custom_settings = {
		'ITEM_PIPELINES': {
			'doubanMovieCrawl.pipelines.ChinieseMovie': 401
		},
		'CONCURRENT_REQUESTS': 100,
		'DOWNLOAD_DELAY': 3,
		'DOWNLOAD_TIMEOUT': 5
	}

	def __init__(self, name=None, **kwargs):
		super().__init__(name=name, **kwargs)
		self.startPage = '0'
		self.headers = settings.Headers

	def start_requests(self):
		doubanMovieURL = settings.MovieURL['chinieseMovie']
		yield scrapy.Request(doubanMovieURL + self.startPage, callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]})

	def parseMovie(self, response):
		print(response.url)
		print(response.status)
		responseBody = response.text
		responseDict = json.loads(responseBody)
		if 'subjects' in responseDict and len(responseDict['subjects']) != 0:
			for eachMovieInfo in responseDict['subjects']:
				item = items.DoubanHighestmoviecrawlItem()
				item['rate'] = eachMovieInfo['rate']
				item['title'] = eachMovieInfo['title']
				item['url'] = eachMovieInfo['url']
				item['cover'] = eachMovieInfo['cover']
				item['id'] = eachMovieInfo['id']
				yield scrapy.Request(item['url'], callback=self.parseSinglePageMovieInfo, headers=self.headers, errback=self.errback_httpbin, meta={'item': item, 'dont_redirect': True, 'handle_httpstatus_list': [302]}, dont_filter=True,)
		responseSplitList = response.url.rsplit('=', 1)
		nextPage = int(responseSplitList[1]) + 20
		nextRequestURL = responseSplitList[0] + '=' + str(nextPage)
		yield scrapy.Request(nextRequestURL, callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]})

	def parseSinglePageMovieInfo(self, response):
		item = response.meta['item']
		selector = response.selector
		item['director'] = '.'.join(selector.xpath(
			'//div[@id="info"]//a[@rel="v:directedBy"]/text()').getall())
		item['actor'] = '/'.join(selector.xpath(
			'//div[@id="info"]//a[@rel="v:starring"]/text()').getall())
		item['genre'] = '/'.join(selector.xpath(
			'//div[@id="info"]//span[@property="v:genre"]/text()').getall())
		item['releaseDate'] = '/'.join(selector.xpath(
			'//div[@id="info"]//span[@property="v:initialReleaseDate"]/text()').getall())
		item['runtime'] = '/'.join(selector.xpath(
			'//div[@id="info"]//span[@property="v:runtime"]/text()').getall())
		hrefs = selector.xpath(
			'//div[@id="info"]//a[@rel="nofollow"]/@href').getall()
		otherNameGroup = re.search(
			r'(?<=又名:</span> )(.*)(?=<br/>)', response.text)
		item['otherName'] = otherNameGroup.group() if otherNameGroup else ''
		languageGroup = re.search(
			r'(?<=语言:</span> )(.*)(?=<br/>)', response.text)
		item['language'] = languageGroup.group() if languageGroup else ''
		produceAreaGroup = re.search(
			r'(?<=制片国家/地区:</span> )(.*)(?=<br/>)', response.text)
		item['produceArea'] = produceAreaGroup.group() if produceAreaGroup else ''
		allTitles = selector.xpath(
			'//div[@id="info"]//span[@class="pl"]/text()').getall()
		if '官方网站:' in allTitles and 'IMDb链接:' not in allTitles:
			item['officialSite'] = hrefs[0]
			item['imdb'] = ''
		elif '官方网站:' not in allTitles and 'IMDb链接:' in allTitles:
			item['officialSite'] = ''
			item['imdb'] = hrefs[0].strip()
		elif '官方网站:' in allTitles and 'IMDb链接:' in allTitles:
			item['officialSite'] = hrefs[0]
			item['imdb'] = hrefs[1].strip()
		else:
			item['officialSite'] = ''
			item['imdb'] = ''
		item['rating_sum'] = selector.xpath(
			'//span[@property="v:votes"]/text()').get()
		item['ratings_on_weight'] = '/'.join(selector.xpath(
			'//div[@class="ratings-on-weight"]//span[@class="rating_per"]/text()').getall())
		if len(selector.xpath(
				'//div[@class="indent"]//span[@class="all hidden"]/text()')) != 0:
			item['summary'] = ''.join(selector.xpath(
				'//div[@class="indent"]//span[@class="all hidden"]/text()').getall()).strip().replace('<br />', '').replace(u'\u3000', u'').replace('\n', '')
		else:
			item['summary'] = ''.join(selector.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()').getall()
									  ).strip().replace('<br />', '').replace(u'\u3000', u'').replace('\n', '')
		awardsGroup = selector.xpath(
			'//div[@class="mod"]//ul[@class="award"]').getall()
		item['award'] = ''
		for award in awardsGroup:
			eachAward = ''
			liLabel = Selector(text=award).xpath('//ul//li').getall()
			for li in liLabel:
				aLabel = Selector(text=li).xpath('//li//a/text()').get()
				if aLabel:
					eachAward += aLabel.strip().replace('\n', '')
				else:
					eachAward += Selector(text=li).xpath(
						'//li/text()').get().strip().replace('\n', '')
				eachAward += '-'
			item['award'] += eachAward + '/'
		item['shortComment'] = '/'.join(selector.xpath(
			'//span[@class="short"]/text()').getall()).strip().replace('\n', '').replace(u'\u3000', u'')
		if len(selector.xpath('//div[@class="tags-body"]')) != 0:
			item['tag'] = '/'.join(selector.xpath(
				'//div[@class="tags-body"]//a/text()').getall())
		similarLike = []
		similarLikeGroups = selector.xpath(
			'//div[@class="recommendations-bd"]//dl').getall()
		for dt in similarLikeGroups:
			group = {}
			group['title'] = Selector(text=dt).xpath('//dd//a/text()').get()
			group['href'] = Selector(text=dt).xpath('//dt//a/@href').get()
			group['img_href'] = Selector(text=dt).xpath('//dt//img/@src').get()
			similarLike.append(group)
		item['similar_like'] = similarLike
		ostFinder = selector.xpath('//div[@class="gray_ad"]//h2/text()').get()
		if '原声' in ostFinder:
			item['ost'] = selector.xpath(
				'//div[@class="gray_ad"]//a/@href').get()
		item['original_photo'] = selector.xpath(
			'//a[@class="nbgnbg"]/@href').get()
		yield item

	def errback_httpbin(self, failure):
		self.logger.error(repr(failure))
