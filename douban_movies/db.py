import pymysql

class DB:

    __host__ = 'localhost'
    __port__ = 3306
    __user_name__ = 'root'
    __password__ = ''
    __db_name__ = 'test'

    __save_tick__ = 20

    create_table_sql = """CREATE TABLE IF NOT EXISTS MOVIES(MOVIE_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,MOVIE_NAME VARCHAR(40),DIRECTOR VARCHAR(40),WRITER VARCHAR(100),ACTORS VARCHAR(200),MOVIE_TYPE VARCHAR(80),LOCATION VARCHAR(40),MOVIE_LANGUAGE VARCHAR(40),MOVIE_TIME VARCHAR(40),MOVE_TIME_LENGTH VARCHAR(40),IMDB_LINK CHAR(40),DESCRIPTION TEXT,RATING FLOAT NOT NULL )"""

    insert_table_sql = """INSERT INTO MOVIES(MOVIE_NAME, DIRECTOR, WRITER, ACTORS, MOVIE_TYPE, LOCATION, MOVIE_LANGUAGE, MOVIE_TIME, MOVE_TIME_LENGTH, IMDB_LINK, DESCRIPTION, RATING) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s','%s', '%f')"""

    select_table_sql = """SELECT IP, PORT FROM IPPROXIES """

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DB, cls).__new__(cls, *args, ** kwargs)
        return cls.__instance

    def __getDb__(self):
        db = pymysql.connect(host=self.__host__, port=self.__port__, user=self.__user_name__, password=self.__password__, db=self.__db_name__, charset='utf8')
        return db

    def __init__(self):
        db = self.__getDb__()
        cursor = db.cursor()
        try:
            cursor.execute(self.create_table_sql)
            db.commit()
            cursor.close()
        finally:
            pass

    def insertMovies(self, movies):
        db = self.__getDb__()
        cursor = db.cursor()


        try:
            if movies is not None:
                for movie in movies:
                    param = (movie.name, movie.getDBStr(movie.director), movie.getDBStr(movie.writer), movie.getDBStr(movie.actors), movie.getDBStr(movie.type), movie.location, movie.getDBStr(movie.language),  movie.getDBStr(movie.time), movie.getDBStr(movie.time_length), movie.imdbLink, movie.description, movie.rating)
                    cursor.execute(self.insert_table_sql% param)
            db.commit()
            cursor.close()
        except:
            db.rollback()
        finally:
            pass

    def getProxies(self):
        db = self.__getDb__()
        cursor = db.cursor()
        proxies = []

        try:
            cursor.execute(self.select_table_sql)
            results = cursor.fetchall()
            if results is not None:
                for row in results:
                    ip = '{0}:{1}'.format(row[0], row[1])
                    proxies.append(ip)

        except Exception as e:
            print(e)
        finally:
            return proxies
