import requests

class Spider(object):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Referer": "https://movie.douban.com/subject",
        "Accept-Encoding": "gzip,deflate,br",
    }

    def __init__(self):
        pass

    def get(self, url):
        try:
            content = requests.get(url, headers=self.headers)
            return content.content
        except:
            print(content.status_code)
        return None