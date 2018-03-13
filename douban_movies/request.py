#请求模块，用于请求对应的链接，使用requests库
import requests
import time

class UrlRequests:
    need_request_url_set = set()
    requested_url_set = set()
    SLEEP_TIME = 2.0


    def __init__(self):
        pass

    def request(self, errorCount = 2):
        url = self.__getUrl__()
        return self.__request__(url)

    def addNeedRequestUrl(self, url):
        allow = self.__checkUrl__(url)
        if allow:
            self.need_request_url_set.add(url)

    def requestNext(self):
        if len(self.need_request_url_set) > 0:
            return True
        return False


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

    def __request__(self, url, errorCount = 2):
        if url is not None:
            try:
                print("go : {0}".format(url))
                time.sleep(self.SLEEP_TIME)
                r = requests.get(url);
                return r.text
            except requests.RequestException as ex:
                print(ex);
                if errorCount > 0:
                    print("go1 : {0}    errorCount : {1}".format(url, errorCount))
                    errorCount -= 1;
                    return self.__request__(url, errorCount)
                else:
                    print("go2 : {0}".format(url))
                    return self.request()
        return None