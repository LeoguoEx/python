
class Urls(object):

    def __init__(self):
        self.urls = set()
        self.requestedUrls = set()

    def addUrl(self, url, append_url):
        if url not in self.requestedUrls:
            self.urls.add(url + append_url)

    def getUrl(self):
        if self.isEnd() is not True:
            url = self.urls.pop()
            self.requestedUrls.add(url)
            return url
        return None

    def urlCount(self):
        return len(self.urls)

    def isEnd(self):
        return self.urlCount() == 0