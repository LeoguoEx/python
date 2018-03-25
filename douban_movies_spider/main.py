from spider import Spider
from ipproxies import IpProxies
from db import DB
from config import Config
import threading
import time
from movie import Movie
import Sqls

class SpiderStarter(object):

    def __init__(self):
        self.spidering = True
        self.movies = []
        self.config = Config()
        self.db = DB(self.config.getData('DBHosts'))
        self.ipproxies = IpProxies()
        self.spider = Spider(self.spider_end_action, self.get_ip_proxies, self.get_requested_urls())
        self.spider.add_request_url('https://movie.douban.com/subject/1292553/?from=subject-page')

    def get_requested_urls(self):
        db = self.db.connectDB()
        cursor = db.cursor()
        cursor.execute(Sqls.select_requested_urls_sql)
        results = cursor.fetchall()
        urls = []
        if results is not None:
            for row in results:
                url = row
                urls.append(url)
        db.close()
        return urls

    def start(self):
        threads = []
        thread = threading.Thread(target=self.scrapy)
        threads.append(thread)
        thread = threading.Thread(target=self.getproxies)
        threads.append(thread)

        for element in threads:
            element.start()

        for element in threads:
            element.join()

    def scrapy(self):
        urls = []
        while self.spidering:
            url = self.spider.get_url()
            html = self.spider.get_next(url)
            movie = Movie()
            new_urls = movie.parseHtml(html)
            self.movies.append(movie)
            self.spider.add_request_urls(new_urls)
            urls.append(url)

            if len(self.movies) > 10:
                db = self.db.connectDB()
                for movie in self.movies:
                    sql = Sqls.insert_table_sql % (movie.name, movie.director, movie.writer, movie.actors, movie.type, \
                                                   movie.location, movie.language, movie.time, movie.time_length, movie.imdbLink, \
                                                   movie.description, movie.rating)
                    self.db.excuteSql(db, sql)
                for element in urls:
                    sql = Sqls.insert_requested_urls_sql % (element)
                    self.db.excuteSql(db, sql)
                self.db.disconnectDB(db)
                self.movies.clear()
                urls.clear()

            time.sleep(3)

    def getproxies(self):
        while self.spidering:
            lock = threading.Lock()
            lock.acquire()
            db = self.db.connectDB()
            cursor = db.cursor()
            cursor.execute(Sqls.select_ip_proxies)
            results = cursor.fetchall()
            proxies = []
            if results is not None:
                for row in results:
                    ip = '{0}:{1}'.format(row[0], row[1])
                    proxies.append(ip)
            db.close()
            self.ipproxies.flushIpProxies(proxies)
            lock.release()
            time.sleep(900)

    def spider_end_action(self):
        self.spidering = False

    def get_ip_proxies(self):
        return self.ipproxies.getProxies()

if __name__ == '__main__':
    starter = SpiderStarter()
    starter.start()
