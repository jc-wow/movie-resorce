import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.high_score_movie import HighScoreMovie
from spiders.chiniese_movie import ChinieseMovie

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(HighScoreMovie)
    process.crawl(ChinieseMovie)
    process.start()
