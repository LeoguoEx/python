#请求模块，用于请求对应的链接，使用requests库
import requests

class UrlRequests:

    need_request_url_set = set()
    requested_url_set = set()

    def __init__(self):
        pass

    def request(self):
        url = self.__getUrl__()
        if url is not None:
            try:
                r = requests.get(url);
                return r.text
            except requests.RequestException as ex:
                print(ex);
        return None

    def addNeedRequestUrl(self, url):
        allow = self.checkUrl(url)
        if allow:
            self.need_request_url_set.add(url)


    def __checkUrl__(self, url):
        allow = url not in self.requested_url_set
        if allow:
            allow = url not in self.need_request_url_set
        return allow

    def __getUrl__(self):
        url = None
        if len(self.need_request_url_set) > 0:
            url = self.need_request_url_set.pop()
        return url;