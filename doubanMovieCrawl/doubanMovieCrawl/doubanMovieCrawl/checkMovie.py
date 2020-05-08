import pymysql

class checkMovie(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'wangchi6992830'
        self.dbName = 'doubanmovie'
        self.charset = 'utf8mb4'
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.passwd,
                                  db=self.dbName,
                                  charset=self.charset
                                  )
        self.cursor = self.db.cursor()
        self.sql = 'SELECT id FROM doubanmovie.movieInfo'
        self.allMovieID = []

    def getMovieID(self):
        try: 
            if self.cursor.connection:
                print('start fetching data')
            else:
                print('retry to reconnect')
                self.cursor = self.db.cursor()  
        except:
            self.sb.rollback()
        finally:
            self.cursor.execute(self.sql)
            self.allMovieID = [item[0] for item in self.cursor.fetchall()]

    def checkMovieInDatabase(self, movieID):
        self.getMovieID()
        if movieID in self.allMovieID:
            print('_______________repeate movie__________________')
            return True
        return False
            
    def __del__(self):
        self.cursor.close()
        self.db.close()

