from lxml import etree
import re

class Movie:

    def __init__(self):
        self.name = ''
        self.director = ''
        self.writer = ''
        self.actors = ''
        self.type = ''
        self.location = ''
        self.language = ''
        self.time = ''
        self.time_length = ''
        self.imdbLink = ''
        self.description = ''
        self.rating = 0.0

    def parseHtml(self, html):
        html = etree.HTML(html)
        parent = '//div[@id="info"]'
        self.name = self.__join__('', self.__get_first_content__(html, '//span[@property="v:itemreviewed"]/text()'))
        self.director = self.__join__(',', html.xpath(parent + '/span[1]/span[@class="attrs"]/a/text()'))
        self.writer = self.__join__(',', html.xpath(parent + '/span[2]/span[@class="attrs"]/a/text()'))
        self.actors = self.__join__(',', html.xpath(parent + '/span[@class="actor"]/span[@class="attrs"]/span/a/text()'))
        self.type = self.__join__(',', html.xpath(parent + '/span[@property="v:genre"]/text()'))
        self.location = self.__join__('', self.__re_content__(r'<span class="pl">制片国家/地区:</span> (.*)<br/>', html, parent))
        self.language = self.__join__(',', self.__getLanguage__(r'<span class="pl">语言:</span> (.*)<br/>', html, parent))
        self.time = self.__join__('', html.xpath(parent + '/span[@property="v:initialReleaseDate"]/text()'))
        self.time_length = self.__join__('', html.xpath(parent + '/span[@property="v:runtime"]/text()'))
        self.imdbLink = self.__join__('', self.__get_first_content__(html, parent + '/a/@href'))
        self.description = self.__get_first_content__(html, '//span[@property="v:summary"]/text()').strip('\r\n ')
        rating = self.__join__('', self.__get_first_content__(html, '//strong[@class="ll rating_num"]/text()'))
        try:
            self.rating = float(rating)
        except Exception as e:
            self.rating = 0.0

        print('name : {0}  type : {1}  language : {2}'.format(self.name, self.type, self.language))
        return self.__get_new_urls__(html)

    def __join__(self, param, list):
        if list is None:
            return ''
        return param.join(list)

    def __get_new_urls__(self, html):
        elements = html.xpath('//div[@class="recommendations-bd"]//@href')
        return elements

    def __re_content__(self, pattern, html, parent):
        findPattern = re.compile(pattern)
        content = html.xpath(parent)
        if len(content) > 0:
            content = etree.tostring(content[0], encoding='utf-8')
            content = content.decode('utf-8')
            content = re.findall(findPattern, content)
            if len(content) > 0:
                return content[0]

    def __getLanguage__(self, pattern, html, parent):
        content = self.__re_content__(pattern, html, parent)
        if content is not None:
            content = content.split(' / ')
        return content

    def __get_first_content__(self, html, path):
        list = html.xpath(path)
        if len(list) > 0:
            return list[0]
        return ""