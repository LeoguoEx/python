#用于数据管理，存入db

from data import DouBanMovie

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
        data = DouBanMovie()
        data.parseHtml(html)
        self.movie_datas.append(data)