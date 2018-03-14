import pymysql
from data import DouBanMovie

class DB:

    __host__ = 'localhost'
    __port__ = 3306
    __user_name__ = 'root'
    __password__ = ''

    __cursor__ = None

    __save_tick__ = 20

    create_table_sql = """CREATE TABLE IF NOT EXISTS MOVIES(
                        MOVIE_NAME CHAR(20) PRIMARY KEY NOT NULL,
                        DIRECTOR CHAR(20),
                        WRITER CHAR(64),
                        ACTORS CHAR(128),
                        MOVIE_TYPE CHAR(20),
                        LOCATION CHAR(10),
                        MOVIE_LANGUAGE CHAR(20),
                        MOVIE_TIME CHAR(20),
                        MOVE_TIME_LENGTH CHAR(10),
                        IMDB_LINK CHAR(40),
                        DESCRIPTION CHAR(600),
                        RATING FLOAT NOT NULL )"""

    insert_table_sql = """INSERT INTO MOVIES(MOVIE_NAME, DIRECTOR, WRITER, ACTORS, MOVIE_TYPE, LOCATION, MOVIE_LANGUAGE, MOVIE_TIME, MOVE_TIME_LENGTH,IMDB_LINK,DESCRIPTION,RATING) VALUES 
                                              ({0}, {1}, {2}, {3}, {4}, {5}, {6},{7}, {8}, {9}, {10}, {11})"""

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DB, cls).__new__(cls, *args, ** kwargs)
        return cls.__instance

    def __init__(self):
        self.getDBCursor()
        self.excuteSql(self.create_table_sql)


    def getDBCursor(self):
        db = pymysql.connect(host=self.__host__, port=self.__port__, user=self.__user_name__, password=self.__password__)
        self.__cursor__ = db.cursor()

    def excuteSql(self, sql):
        if self.__cursor__ is not None:
            self.__cursor__.execute(sql)

    def insertMovieInfo(self, movie):
        if movie is not None and movie is DouBanMovie:
            movie = DouBanMovie()
            sql = self.insert_table_sql.format(movie.name, movie.director, movie.actors, movie.type, movie.location, movie.language, movie.time, movie.time_length,
                                               movie.imdbLink, movie.description, movie.rating)
            self.excuteSql(sql)

    def update(self):
        pass