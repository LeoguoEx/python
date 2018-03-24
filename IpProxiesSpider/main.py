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

    time.sleep(crawler_data.per_link_sleep_time)

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
        success = telnetTest.telnetTest(proxie, crawler_data.telnet_time_out)
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
        for i in range(crawler_data.crawler_page_min, crawler_data.crawler_page_max):
            urls.addUrl('http://www.xicidaili.com', '/nn/{0}'.format(i))
        beginCrawler()
        print(len(proxies_list))
        printAvailableProxies(proxies_list)
        saveToDB(proxies_list)
        time.sleep(crawler_data.sleep_time)


crawler_data = None
urls = None
spider = None
telnetTest = None
config = None
db = None
proxies_list = None
if __name__ == '__main__':
    config = Config()
    crawler_data = config.getData('CrawlerStruct')
    db = DB(config.getData('DBHosts'))
    urls = Urls()
    spider = Spider()
    telnetTest = TelnetTest()
    proxies_list = []
    main()