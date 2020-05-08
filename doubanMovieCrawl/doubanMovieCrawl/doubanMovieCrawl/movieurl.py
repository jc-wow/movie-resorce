class URL(object):
    def __init__(self):
        self.__allMovie = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='
        # self.__doubanHighScoreMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=time&page_limit=20&page_start='
        # self.__doubanLowWatchButWellMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&sort=time&page_limit=20&page_start='
        # self.__doubanHotMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
        # self.__doubanNewestMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start='
        # self.__doubanClassicMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=20&page_start='
        # self.__doubanVideoedMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8F%AF%E6%92%AD%E6%94%BE&sort=time&page_limit=20&page_start='
        # self.__doubanChineseMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=time&page_limit=20&page_start='
        # self.__doubanEnglishMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%AC%A7%E7%BE%8E&sort=time&page_limit=20&page_start='
        # self.__doubanKoreaMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E9%9F%A9%E5%9B%BD&sort=time&page_limit=20&page_start='
        # self.__doubanJapanMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&sort=time&page_limit=20&page_start='
        # self.__doubanActionMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8A%A8%E4%BD%9C&sort=time&page_limit=20&page_start='
        # self.__doubanComedyMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%96%9C%E5%89%A7&sort=time&page_limit=20&page_start='
        # self.__doubanLoveMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort=time&page_limit=20&page_start='
        # self.__doubanScienceMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=time&page_limit=20&page_start='
        # self.__doubanSuspenceMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%82%AC%E7%96%91&sort=time&page_limit=20&page_start='
        # self.__doubanHorribleMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%81%90%E6%80%96&sort=time&page_limit=20&page_start='
        # self.__doubanCartoonMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8A%A8%E7%94%BB&sort=time&page_limit=20&page_start='
   
    def getAllMovieURL(self):
        return [
            self.__allMovie
            # self.__doubanHighScoreMovieURL,
            # self.__doubanLowWatchButWellMovieURL,
            # self.__doubanHotMovieURL,
            # self.__doubanNewestMovieURL,
            # self.__doubanClassicMovieURL,
            # self.__doubanVideoedMovieURL,
            # self.__doubanChineseMovieURL,
            # self.__doubanEnglishMovieURL,
            # self.__doubanKoreaMovieURL,
            # self.__doubanJapanMovieURL,
            # self.__doubanActionMovieURL,
            # self.__doubanComedyMovieURL,
            # self.__doubanLoveMovieURL,
            # self.__doubanScienceMovieURL,
            # self.__doubanSuspenceMovieURL,
            # self.__doubanHorribleMovieURL,
            # self.__doubanCartoonMovieURL
        ]