class URL(object):
    def __init__(self):
        self.__allMovie = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags='
   
    def getAllMovieURL(self, tag):
        return self.__allMovie + tag + '&start='