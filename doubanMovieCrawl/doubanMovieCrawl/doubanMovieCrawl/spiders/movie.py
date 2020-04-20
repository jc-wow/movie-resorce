import pymysql
from scrapy.selector import Selector
import json
import re
from doubanMovieCrawl import movieurl
from doubanMovieCrawl import items
import scrapy
import sys
sys.path.append('..')


class Movie(scrapy.Spider):
    name = 'doubanMovieCrawl'
    allowed_domains = ['douban.com']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        self.startPage = 0
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/explore',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def getDoubanHighScoreMovieURL(self):
        movieURL = movieurl.URL()
        return movieURL.getDoubanHighScoreMovieUrl()

    def getDoubanLowWatchButWellMovieURL(self):
        movieURL = movieurl.URL()
        return movieURL.getDoubanLowWatchButWellMovieURL()

    def getValidProxy(self):
        pass

    def start_requests(self):
        self.highScoreURL = self.getDoubanHighScoreMovieURL()
        self.lowWatchButWellMovieURL = self.getDoubanLowWatchButWellMovieURL()
        yield scrapy.Request(self.highScoreURL + str(self.startPage), callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin)
        yield scrapy.Request(self.lowWatchButWellMovieURL + str(self.startPage), callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin)

    def parseMovie(self, response):
        self.logger.info('high score movie: %s', response.url)
        self.logger.info("current user-agent: %s",
                         response.request.headers['User-Agent'])
        if not response:
            return
        responseBody = response.text
        responseDict = json.loads(responseBody)
        if responseDict and 'subjects' in responseDict:
            self.startPage += 1
            for eachMovieInfo in responseDict['subjects']:
                item = items.DoubanHighestmoviecrawlItem()
                item['rate'] = eachMovieInfo['rate']
                item['title'] = eachMovieInfo['title']
                item['url'] = eachMovieInfo['url']
                item['cover'] = eachMovieInfo['cover']
                item['id'] = eachMovieInfo['id']
                yield scrapy.Request(item['url'], callback=self.parseSinglePageMovieInfo, headers=self.headers, errback=self.errback_httpbin, meta={'item': item})
            yield scrapy.Request(self.highScoreURL + str(self.startPage), callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin)

    def parseSinglePageMovieInfo(self, response):
        self.logger.info("current user-agent: %s",
                         response.request.headers['User-Agent'])
        self.logger.info("current ip: %s",
                         response.request.headers['proxy'])
        self.logger.info('similar movie: %s', response.url)
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
            item['officalSite'] = hrefs[0]
            item['imdb'] = ''
        elif '官方网站:' not in allTitles and 'IMDb链接:' in allTitles:
            item['officalSite'] = ''
            item['imdb'] = hrefs[0]
        elif '官方网站:' in allTitles and 'IMDb链接:' in allTitles:
            item['officalSite'] = hrefs[0]
            item['imdb'] = hrefs[1]
        else:
            item['officalSite'] = ''
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
            '//span[@class="short"]/text()').getall()).strip().replace('\n', '')

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))

    def conn(self):
        mydb = pymysql.Connect('localhost', 'root', 'password',
                               'demo_db', autocommit=True)
        return mydb.cursor()

    def getProxyFromDatabase(self, query, c):
        try:
            if c.connection:
                print("connection exists")
                c.execute(query)
                return c.fetchall()
            else:
                print("trying to reconnect")
                c = self.conn()
        except Exception as e:
            return str(e)
