import pymysql
from data import DouBanMovie

class DB:

    __host__ = 'localhost'
    __port__ = 3306
    __user_name__ = 'root'
    __password__ = ''
    __db_name__ = 'test'

    __save_tick__ = 20

    create_table_sql = """CREATE TABLE IF NOT EXISTS MOVIES(MOVIE_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,MOVIE_NAME VARCHAR(20),DIRECTOR VARCHAR(40),WRITER VARCHAR(40),ACTORS VARCHAR(64),MOVIE_TYPE VARCHAR(20),LOCATION VARCHAR(20),MOVIE_LANGUAGE VARCHAR(20),MOVIE_TIME VARCHAR(20),MOVE_TIME_LENGTH VARCHAR(20),IMDB_LINK CHAR(40),DESCRIPTION TEXT,RATING FLOAT NOT NULL )"""

    insert_table_sql = """INSERT INTO MOVIES(MOVIE_NAME, DIRECTOR, WRITER, ACTORS, MOVIE_TYPE, LOCATION, MOVIE_LANGUAGE, MOVIE_TIME, MOVE_TIME_LENGTH, IMDB_LINK, DESCRIPTION, RATING) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %f)"""

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

        if movies is not None:
            for movie in movies:
                param = (movie.name, ','.join(movie.director), ','.join(movie.writer), ','.join(movie.actors), ','.join(movie.type), movie.location, ','.join(movie.language),  ','.join(movie.time),  ','.join(movie.time_length), movie.imdbLink, movie.description, movie.rating)
                cursor.execute(self.insert_table_sql, param)
        db.commit()
        cursor.close()
        '''
        try:
            if movies is not None:
                for movie in movies:
                    param = (movie.name, movie.director, movie.writer, movie.actors, movie.type, movie.location, movie.language, movie.time, movie.time_length, movie.imdbLink, movie.description, movie.rating)
                    cursor.execute(self.insert_table_sql % param)
            db.commit()
            cursor.close()
        except:
            db.rollback()
        finally:
            pass
        '''