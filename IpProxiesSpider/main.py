from Spider import Spider
from IPProxies import IPProxie
from Urls import Urls
from TelnetTest import TelnetTest
from Config import Config
from DB import DB
import time
import Sqls


def printAvailableProxies(proxies):
    for proxie in proxies:
        proxie.printProxie()


def beginCrawler():
    content = getRightContent()
    if content is not None:
        proxies = getIPProxies(content)
        proxies_list.extend(proxies)

    time.sleep(per_link_sleep_time)

    if urls.isEnd() is not True:
        beginCrawler()
    else:
        pass


def getRightContent():
    if urls.isEnd() is not True:
        url = urls.getUrl()
        print('url = {0}'.format(url))
        content = spider.get(url)
        if content is None:
            return getRightContent()
        return content
    return None


def getIPProxies(content):
    proxies = IPProxie.parse(content)
    return testIPProxies(proxies)


def testIPProxies(proxies):
    list = []
    for proxie in proxies:
        success = telnetTest.telnetTest(proxie)
        if success:
            list.append(proxie)
    return list


def saveToDB(proxies):
    curdb = db.connectDB()
    db.excuteSql(curdb, Sqls.TRUNCATE)
    for data in proxies:
        db.excuteSql(curdb, Sqls.INSERT_TABLE % (data.ip, data.port, data.protocol, data.speed, data.connect_time))
    db.disconnectDB(curdb)


def main():
    while True:
        for i in range(1, crawler_max_page_count):
            urls.addUrl('http://www.xicidaili.com', '/nn/{0}'.format(i))
        beginCrawler()
        print(len(proxies_list))
        printAvailableProxies(proxies_list)
        saveToDB(proxies_list)
        time.sleep(sleep_time)


crawler_max_page_count = None
sleep_time = None
per_link_sleep_time = None
urls = None
spider = None
telnetTest = None
config = None
db = None
proxies_list = None
if __name__ == '__main__':
    crawler_max_page_count = 9
    sleep_time = 900
    per_link_sleep_time = 0.5
    config = Config()
    db = DB(config.dbhosts)
    urls = Urls()
    spider = Spider()
    telnetTest = TelnetTest()
    proxies_list = []
    main()