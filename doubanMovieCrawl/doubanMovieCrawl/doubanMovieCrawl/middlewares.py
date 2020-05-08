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

class RandomUserAgentMiddleware(object):
    logger = logging.getLogger(__name__)
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.validProxy = []
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
            'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.testurl="https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=10"

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        if len(self.validProxy) != 0:
            print(self.validProxy)
            validProxy = self.validProxy[0]
            request.meta['proxy'] = 'http://' + validProxy
        else:  
            proxy = self.getProxyFromDatabase()
            validProxy = self.getValidProxy(proxy)
            request.meta['proxy'] = 'http://' + validProxy
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

    def getProxyFromDatabase(self):
        res = requests.get("http://127.0.0.1:5011/get/", timeout=10).json()
        time.sleep(2)
        if 'code' in res and res['code'] == 0:
            print('retry to local proxy database......')
            self.getProxyFromDatabase()
        else:
            proxy = res['proxy']
        return proxy
    
    def getValidProxy(self, proxy):
        isValid = self.testProxyValid(proxy)
        if isValid == 1:
            return proxy
        else:
            self.handleTestProxyNextStep(proxy)
            newProxy = self.getProxyFromDatabase()
            return self.getValidProxy(newProxy)
                 
    def testProxyValid(self, proxy):
        validNum = 0
        print('test current proxy valid......')
        ip = {"http": "http://" + proxy, "https": "https://" + proxy}
        try:     
            r = requests.get(url=self.testurl, headers=self.headers, proxies=ip, timeout=5)
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
        if proxy in self.validProxy: 
            self.validProxy.remove(proxy)
        self.delete_proxy(proxy)

    def process_response(self, request, response, spider):
        if response.status != 200:
            proxy = self.getProxyFromDatabase()
            validProxy = self.getValidProxy(proxy)
            request.meta['proxy'] = 'http://' + validProxy
            return request
        return response

    def process_exception(self, request, exception, spider):
        logging.exception(exception)
        return request

    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5011/delete/?proxy={}".format(proxy))

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
