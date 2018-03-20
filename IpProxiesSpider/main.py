import time
import Spider
import IPProxies
import Urls

def getIPProxies():
    pass

def main():
    for i in 9:
        urls.addUrl('http://www.xicidaili.com', '/nn/{0}'.format(i+1))

    while urls.isEnd() is not True:
        url = urls.getUrl()
        content = spider.get(url)
        if content is None:
            pass


urls = Urls()
spider = Spider()
if __name__ == '__main__':
    main()