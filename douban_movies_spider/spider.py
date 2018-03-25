import requests

class Spider(object):

    def __init__(self, action, ip_proxie_action, resquested_urls):
        self.headers =  {
                            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
                            "Accept-Encoding" : "gzip,deflate,br",
                        }

        self.need_requests_url = set()
        self.requested_url = set()
        for url in resquested_urls:
            self.requested_url.add(url)
        self.action = action
        self.ip_proxie_action = ip_proxie_action

    def get_next(self, url):
        content = None
        if url is not None:
            ip_prox = self.ip_proxie_action()
            print('url : {0}     prox : {1}'.format(url, ip_prox))
            prox = {'http' : 'http://' + ip_prox}
            content = requests.get(url, headers =self.headers, proxies=prox)
            content = content.content.decode(encoding='utf-8')
        return content

    def add_request_url(self, url):
        if url is None or url == '':
            return
        if url in self.requested_url:
            return
        if url in self.need_requests_url:
            return
        self.need_requests_url.add(url)

    def add_request_urls(self, urls):
        if urls is not None:
            for url in urls:
                self.add_request_url(url)

    def get_url(self):
        if len(self.need_requests_url) > 0:
            url = self.need_requests_url.pop()
            self.requested_url.add(url)
            return url
        else:
            if self.action is not None:
                self.action()
            return None