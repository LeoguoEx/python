#用于数据管理，存入db

from data import DouBanMovie
from db import DB
from lxml import etree

class DataManager:

    movie_datas = []

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        pass

    def parseHtml(self, html):
        html = etree.HTML(html)
        data = DouBanMovie()
        data.parseHtml(html)
        self.movie_datas.append(data)
        self.__writeToDB__()

    def __writeToDB__(self):
         if len(self.movie_datas) > 10:
            db = DB()
            db.insertMovies(self.movie_datas)
            self.movie_datas.clear()