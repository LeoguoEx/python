import pymysql
from data import DouBanMovie

class DB:

    __host__ = 'localhost'
    __port__ = 3306
    __user_name__ = 'root'
    __password__ = ''
    __db_name__ = 'test'

    __save_tick__ = 20

    create_table_sql = """CREATE TABLE IF NOT EXISTS MOVIES(
                        MOVIE_NAME CHAR(20) PRIMARY KEY NOT NULL,
                        DIRECTOR CHAR(20),
                        WRITER CHAR(64),
                        ACTORS CHAR(128),
                        MOVIE_TYPE CHAR(20),
                        LOCATION CHAR(10),
                        MOVIE_LANGUAGE CHAR(40),
                        MOVIE_TIME CHAR(20),
                        MOVE_TIME_LENGTH CHAR(10),
                        IMDB_LINK CHAR(40),
                        DESCRIPTION TEXT,
                        RATING FLOAT NOT NULL )"""

    insert_table_sql = """INSERT INTO MOVIES VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %f)"""

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
                cursor.execute(self.insert_table_sql % param)
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