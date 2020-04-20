class URL(object):
    def __init__(self):
        self.__doubanHighScoreMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start='
        self.__doubanLowWatchButWellMovieURL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&page_limit=50&page_start='

    def getDoubanHighScoreMovieUrl(self):
        return self.__doubanHighScoreMovieURL

    def getDoubanLowWatchButWellMovieURL(self):
        return self.__doubanLowWatchButWellMovieURL