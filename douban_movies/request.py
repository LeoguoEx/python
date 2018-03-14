#请求模块，用于请求对应的链接，使用requests库
import requests
import time

class UrlRequests:
    need_request_url_set = set()
    requested_url_set = set()
    request_end_action = None

    SLEEP_TIME = 2.0
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Referer" : "https://movie.douban.com/subject",
        "Accept-Encoding" : "gzip,deflate,br",
    }
    #cookies = 'viewed="1770782_27608197_25779298_10561367_26791779_2667007"; bid=a6qaOnTmw2Q; gr_user_id=a028857d-f762-4168-a994-7354ea3ba43a; __utma=30149280.612941763.1516353592.1520934637.1520997353.12; __utmz=30149280.1520934637.11.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _vwo_uuid_v2=3BE36ADECB0EDF3CE0D959A305BC8602|a1d79284fa96cab9b9f257fad0c93f5f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1520997350%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2Fqijiuzhiyue%2F%22%5D; _pk_id.100001.4cf6=6d96ddf160dab611.1519091449.8.1520997989.1520925914.; __utma=223695111.1111103676.1519091451.1520911009.1520997353.7; __utmz=223695111.1520908773.5.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/qijiuzhiyue/; ap=1; __yadk_uid=9bTu0C3HMjGPVonBiTF70BsMZq4tTwSt; ll="108288"; __utmc=30149280; __utmc=223695111; _pk_ses.100001.4cf6=*; __utmb=30149280.1.10.1520997353; __utmb=223695111.0.10.1520997353; __utmt=1; report=ref=%2F&from=mv_a_pst'

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(UrlRequests, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        pass

    def request(self):
        url = self.__getUrl__()
        html = self.__request__(url)
        if self.request_end_action is not None:
            self.request_end_action(html)

    def addNeedRequestUrl(self, url):
        allow = self.__checkUrl__(url)
        if allow:
            self.need_request_url_set.add(url)

    def requestNext(self):
        if len(self.need_request_url_set) > 0:
            return True
        return False

    def setRequestEndAction(self, action):
        self.request_end_action = action

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
                time.sleep(self.SLEEP_TIME)
                print("request url : {0}".format(url))
                r = requests.get(url, headers=self.headers);
                return r.content
            except requests.RequestException as ex:
                if errorCount > 0:
                    errorCount -= 1;
                    return self.__request__(url, errorCount)
                else:
                    return self.request()
        return None