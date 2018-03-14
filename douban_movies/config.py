#一些静态数据的存储，解析配置文件

import csv

class ConfigManager:

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        pass

    def initFileHeader(self):

        name = None
        director = None
        writer = None
        actors = None
        type = None
        location = None
        language = None
        time = None
        time_length = None
        imdbLink = None
        description = None
        rating = None

    def saveDouBanMoviesInfoToFile(movies):
        # TODO:将豆瓣的电影信息写入文件
        with open('DouBanMovieTop250.csv', 'w+', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['排名', '名称', '评分', '评价', '简介', '链接'])
            for movieInfo in d.values():
                writer.writerow([movieInfo.getRank(),
                                 movieInfo.getMovieName(),
                                 movieInfo.getScore(),
                                 movieInfo.getEstimate(),
                                 movieInfo.getQuote(),
                                 movieInfo.getLink()])
        csvfile.close()