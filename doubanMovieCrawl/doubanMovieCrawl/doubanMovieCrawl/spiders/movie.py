from scrapy.selector import Selector
import json
import re
from doubanMovieCrawl import movieurl
from doubanMovieCrawl import items
from doubanMovieCrawl import checkMovie
from scrapy import FormRequest
import scrapy
import sys
sys.path.append('..')


class Movie(scrapy.Spider):
    name = 'doubanMovieCrawl'
    allowed_domains = ['douban.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        self.startPage = '4100'
        self.tags = ['电影', '电视剧', '综艺', '动漫', '纪录片', '短片']
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/tag/',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Accept-Encoding': 'utf8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

    def getDoubanMovieURL(self, tag):
        movieURL = movieurl.URL()
        return movieURL.getAllMovieURL(tag)

    def start_requests(self):
        for tag in self.tags:
            doubanMovieURL = self.getDoubanMovieURL(tag)
            yield scrapy.Request(doubanMovieURL + self.startPage, callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True, 'handle_httpstatus_list': [302], 'item': tag})

    def checkMovieInDatabase(self, movieID):
        return checkMovie.checkMovie().checkMovieInDatabase(movieID)

    def parseMovie(self, response):
        print(response.url)
        print(response.status)
        responseBody = response.text
        responseDict = json.loads(responseBody)
        tag = response.meta['item']
        if 'r' in responseDict and responseDict['r'] == 1:
            print('spider encounter some trouble')
            print(responseDict)
        if responseDict and 'data' in responseDict:
            for eachMovieInfo in responseDict['data']:
                item = items.DoubanHighestmoviecrawlItem()
                item['rate'] = eachMovieInfo['rate']
                item['title'] = eachMovieInfo['title']
                item['url'] = eachMovieInfo['url']
                item['cover'] = eachMovieInfo['cover']
                item['id'] = eachMovieInfo['id']
                item['tag'] = tag
                # if self.checkMovieInDatabase(item['id']): continue
                yield scrapy.Request(item['url'], callback=self.parseSinglePageMovieInfo, headers=self.headers, errback=self.errback_httpbin, meta={'item': item, 'dont_redirect': True, 'handle_httpstatus_list': [302]}, dont_filter=True,)
        responseSplitList = response.url.rsplit('=', 1)
        nextPage = int(responseSplitList[1]) + 20
        nextRequestURL = responseSplitList[0] + '=' + str(nextPage)
        yield scrapy.Request(nextRequestURL, callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True, 'handle_httpstatus_list': [302], 'item': tag})

    def parseSinglePageMovieInfo(self, response):
        print('start parsing movieInfo')
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
        yield item

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))
