from lxml import etree
import re
from request import UrlRequests

class DouBanMovie:

    name = None
    director = None
    writer = None
    actors = None
    type = None
    location = None
    language = None
    time = None
    time_length = None
    imdbLink = None
    description = None
    rating = None


    def __init__(self):
        pass

    def parseHtml(self, html):
        self.name = self.__get_first_content__(html, '//span[@property="v:itemreviewed"]/text()')
        self.__getDivInfo__(html)
        self.description = self.__get_first_content__(html, '//span[@property="v:summary"]/text()').strip('\r\n ')
        rating = self.__get_first_content__(html, '//strong[@class="ll rating_num"]/text()')
        try:
            self.rating = float(rating)
        except:
            self.rating = 0.0
        self.__add_next_url__(html)

    def print(self):
        print("name : {0}".format(self.name))
        print("director : {0}".format(self.director))
        print("writer : {0}".format(self.writer))
        print("actors : {0}".format(self.actors))
        print("type : {0}".format(self.type))
        print("location : {0}".format(self.location))
        print("language : {0}".format(self.language))
        print("time : {0}".format(self.time))
        print("time_length : {0}".format(self.time_length))
        print("imdbLink : {0}".format(self.imdbLink))
        print("description : {0}".format(self.description))
        print("rating : {0}".format(self.rating))

    def __add_next_url__(self, html):
        elements = self.__getcontent__(html, '', '//div[@class="recommendations-bd"]//@href')
        request = UrlRequests()
        for element in elements:
            request.addNeedRequestUrl(element)

    def __get_first_content__(self, html, path):
        list = html.xpath(path)
        if len(list) > 0:
            return list[0]
        return ""

    def __getcontent__(self, html, parent, append):
        path = parent + append
        content = html.xpath(path)
        return content

    def __re_content__(self, pattern, html, parent):
        findPattern = re.compile(pattern)
        content = html.xpath(parent)
        if len(content) > 0:
            content = etree.tostring(content[0], encoding='utf-8')
            content = content.decode('utf-8')
            content = re.findall(findPattern, content)
            if len(content) > 0:
                return content[0]

    def __getDivInfo__(self, html):
        parent = '//div[@id="info"]'
        self.director = self.__getcontent__(html, parent,  '/span[1]/span[@class="attrs"]/a/text()')
        self.writer = self.__getcontent__(html, parent, '/span[2]/span[@class="attrs"]/a/text()')
        self.actors = self.__getcontent__(html, parent, '/span[3]/span[@class="attrs"]/span/a/text()')
        self.type = self.__getcontent__(html, parent, '/span[@property="v:genre"]/text()')
        self.time = self.__getcontent__(html, parent, '/span[@property="v:initialReleaseDate"]/text()')
        self.time_length = self.__getcontent__(html, parent, '/span[@property="v:runtime"]/text()')
        self.imdbLink = self.__get_first_content__(html, parent + '/a/@href')
        self.location = self.__re_content__(r'<span class="pl">制片国家/地区:</span> (.*)<br/>', html, parent)
        self.__getLanguage__(r'<span class="pl">语言:</span> (.*)<br/>', html, parent)


    def __getLanguage__(self, pattern, html, parent):
        content = self.__re_content__(pattern, html, parent)
        content = content.split(' / ')
        self.language = content
