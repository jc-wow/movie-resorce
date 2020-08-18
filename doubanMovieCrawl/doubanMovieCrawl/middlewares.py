# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import logging
import json
import time
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random


class RandomProxyMiddleware(object):
    logger = logging.getLogger(__name__)

    def __init__(self, crawler):
        super(RandomProxyMiddleware, self).__init__()
        self.validProxy = []
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Accept-Encoding': 'utf8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        self.testurl = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=10"

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        try:
            if len(self.validProxy) != 0:
                print(self.validProxy)
                validProxy = self.validProxy[0]
                request.meta['proxy'] = 'http://' + validProxy
            else:
                proxy = self.getProxyFromDatabase()
                validProxy = self.getValidProxy(proxy)
                request.meta['proxy'] = 'http://' + validProxy
        except Exception as e:
            logging.error(e)
            proxy = request.meta['proxy']
            self.handleTestProxyNextStep(proxy)
            return request

    def getProxyFromDatabase(self):
        res = requests.get("http://localhost:5010/get/", timeout=5).json()
        time.sleep(2)
        try:
            if 'code' in res and res['code'] == 0:
                print('retry to local proxy database......')
                self.validProxy = []
                self.getProxyFromDatabase()
            else:
                proxy = res['proxy']
            return proxy
        except Exception as e:
            logging.error(e)

    def getValidProxy(self, proxy):
        isValid = self.testProxyValid(proxy)
        if isValid == 1:
            if proxy not in self.validProxy:
                self.validProxy.append(proxy)
            return proxy
        else:
            self.handleTestProxyNextStep(proxy)
            newProxy = self.getProxyFromDatabase()
            return self.getValidProxy(newProxy)

    def testProxyValid(self, proxy):
        validNum = 0
        print('test current proxy valid......')
        ip = {"http": "http://" + proxy, "https": "https://" + proxy}
        ua = UserAgent()
        self.headers['User-Agent'] = ua.random
        try:
            r = requests.get(url=self.testurl,
                             headers=self.headers, proxies=ip, timeout=5)
            print(r.status_code)
            responseDict = json.loads(r.text)
            if r.status_code == 200:
                if 'msg' in responseDict and 'r' in responseDict and responseDict['r'] == 1:
                    print(responseDict)
                    validNum = 0
                else:
                    validNum = 1
            else:
                validNum = 0
        except Exception as e:
            logging.warn(e)
            validNum = 0
        return validNum

    def handleTestProxyNextStep(self, proxy):
        print('remove proxy from list')
        if '/' in proxy:
            proxySplitList = proxy.rsplit('/', 1)
            proxy = proxySplitList[1]
        print('remove proxy:' + proxy)
        if proxy in self.validProxy:
            self.validProxy.remove(proxy)
        self.delete_proxy(proxy)

    def process_response(self, request, response, spider):
        print('get response from middleware')
        print(request.meta['proxy'])
        proxy = request.meta['proxy']
        try:
            responseText = response.text
            if response.status != 200 or ('msg' in responseText and 'r' in responseText):
                print(response.text)
                self.handleTestProxyNextStep(proxy)
                newProxy = self.getProxyFromDatabase()
                validProxy = self.getValidProxy(newProxy)
                request.meta['proxy'] = 'http://' + validProxy
                return request
            return response
        except Exception as e:
            logging.error(e)
            self.handleTestProxyNextStep(proxy)
            return request

    def process_exception(self, request, exception, spider):
        logging.exception(exception)
        proxy = request.meta['proxy']
        self.handleTestProxyNextStep(proxy)
        return request

    def delete_proxy(self, proxy):
        requests.get("http://localhost:5010/delete/?proxy={}".format(proxy))


class DoubanmoviecrawlSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanmoviecrawlDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
