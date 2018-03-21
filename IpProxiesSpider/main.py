from Spider import Spider
from IPProxies import IPProxie
from Urls import Urls
from TelnetTest import TelnetTest
import logging
import time


def infoPrinter(func):
    def wrapper(*args):
        logging.warning('%s is running' % func.__name__)
        return func(*args)
    return wrapper


#@infoPrinter
def printAvailableProxies(proxies):
    for proxie in proxies:
        proxie.printProxie()


@infoPrinter
def beginCrawler():
    content = getRightContent()
    if content is not None:
        proxies = getIPProxies(content)
        proxies_list.extend(proxies)

    if urls.isEnd() is not True:
        beginCrawler()
    else:
        pass



#@infoPrinter
def getRightContent():
    if urls.isEnd() is not True:
        url = urls.getUrl()
        print('url = {0}'.format(url))
        content = spider.get(url)
        if content is None:
            return getRightContent()
        return content
    return None


#@infoPrinter
def getIPProxies(content):
    proxies = IPProxie.parse(content)
    return testIPProxies(proxies)


#@infoPrinter
def testIPProxies(proxies):
    list = []
    for proxie in proxies:
        success = telnetTest.telnetTest(proxie)
        if success:
            list.append(proxie)
    return list


def main():
    while True:
        for i in range(1, crawler_max_page_count):
            urls.addUrl('http://www.xicidaili.com', '/nn/{0}'.format(i))
        beginCrawler()
        print(len(proxies_list))
        printAvailableProxies(proxies_list)
        time.sleep(sleep_time)


crawler_max_page_count = None
sleep_time = None
urls = None
spider = None
telnetTest = None
proxies_list = None
if __name__ == '__main__':
    crawler_max_page_count = 9
    sleep_time = 900
    urls = Urls()
    spider = Spider()
    telnetTest = TelnetTest()
    proxies_list = []
    main()