class CrawlerStruct(object):

    def __init__(self):
        self.crawler_page_min = 1
        self.crawler_page_max = 9
        self.per_link_sleep_time = 0.5
        self.crawler_sleep_time = 900
        self.telnet_time_out = 3

    def getDict(self):
        dic = {"crawler_page_min" : self.crawler_page_min,
               "crawler_page_max" : self.crawler_page_max,
               "per_link_sleep_time" : self.per_link_sleep_time,
               "crawler_sleep_time": self.crawler_sleep_time,
               "telnet_time_out" : self.telnet_time_out
               }
        return dic

    def setDict(self, dic):
        if dic is None:
            return False
        self.crawler_page_min = dic["crawler_page_min"]
        self.crawler_page_max = dic["crawler_page_max"]
        self.per_link_sleep_time = dic["per_link_sleep_time"]
        self.crawler_sleep_time = dic["crawler_sleep_time"]
        self.telnet_time_out = dic["telnet_time_out"]
        return True