import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.europe_movie import EuropeMovie
from spiders.japan_movie import JapanMovie
from spiders.korea_movie import KoreaMovie

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(EuropeMovie)
    process.crawl(JapanMovie)
    process.crawl(KoreaMovie)
    process.start()
