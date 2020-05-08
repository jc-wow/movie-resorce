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
        self.cookie = 'll="118238"; bid=tFRyBl3qM28; __gads=ID=2faa0d99b0f90e56:T=1588318308:S=ALNI_Maya9lPl2siBOL-lGjGQgF19WV0lQ; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17822; _vwo_uuid_v2=DF06579EEBD8635FF88ECF459BEDCE496|62d0e51b17c697fd780a03dad70248f5; douban-fav-remind=1; __utmc=30149280; ap_v=0,6.0; __utma=30149280.289087522.1588318292.1588750721.1588752696.12; __utmz=30149280.1588752696.12.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; apiKey=; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1588753234%2C%22https%3A%2F%2Fmovie.douban.com%2Ftag%2F%22%5D; _pk_ses.100001.2fad=*; __utmb=30149280.5.8.1588753478333; last_login_way=account; _pk_id.100001.2fad=93265dcefa7cd458.1588753234.1.1588754465.1588753234.; login_start_time=1588754470181'
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/tag/',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Accept-Encoding': 'utf8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Cookie': self.cookie
        }
        
    def getDoubanMovieURL(self):
        movieURL = movieurl.URL()
        return movieURL.getAllMovieURL()      

    def start_requests(self):
        self.doubanMovieURL = self.getDoubanMovieURL()
        for url in self.doubanMovieURL:
            yield scrapy.Request(url + '8080', callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter=True, meta={'dont_redirect': True,'handle_httpstatus_list': [302]})
    
    def checkMovieInDatabase(self, movieID):
        return checkMovie.checkMovie().checkMovieInDatabase(movieID)
        
    def parseMovie(self, response):
        print(response.url)
        print(response.status)
        responseBody = response.text
        responseDict = json.loads(responseBody)
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
                if self.checkMovieInDatabase(item['id']): continue
                yield scrapy.Request(item['url'], callback=self.parseSinglePageMovieInfo, headers=self.headers, errback=self.errback_httpbin, meta={'item': item, 'dont_redirect': True,'handle_httpstatus_list': [302]}, dont_filter = True,)
        responseSplitList = response.url.rsplit('=', 1)
        nextPage = int(responseSplitList[1]) + 20
        nextRequestURL = responseSplitList[0] + '=' + str(nextPage)
        yield scrapy.Request(nextRequestURL, callback=self.parseMovie, headers=self.headers, errback=self.errback_httpbin, dont_filter = True ,meta={'dont_redirect': True,'handle_httpstatus_list': [302]})

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

