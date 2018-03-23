import requests

class Spider(object):

    headers = {
        #"Accept":'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        "Accept-Encoding": "gzip,deflate",
        "Connection":"keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    }
    cookies = "Hm_lvt_0cf76c77469e965d2957f05…5d2957f0553e6ecf59=1521513257"

    def __init__(self):
        pass

    def get(self, url):
        content = requests.get(url, headers=self.headers)
        content = content.content.decode(encoding='utf-8')
        return content

        '''        
        try:
            self.headers["Referer"] = str(url)
            content = requests.get(url, headers=self.headers)
            content = content.content.decode(encoding='utf-8')
            return content
        except Exception as e:
            print(e)
            return None
        '''

