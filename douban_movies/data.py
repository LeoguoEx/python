from lxml import etree
import re

class DouBanMovie:

    name = ""
    director = []
    writer = []
    actors = []
    type = []
    location = ""
    language = []
    time = []
    time_length = []
    imdbLink = ""
    description = ""


    def __init__(self):
        pass

    def parseHtml(self, text):
        html = text
        list = html.xpath('//span[@property="v:itemreviewed"]/text()')
        if len(list) > 0:
            self.name = list[0]

        self.__getDivInfo__(html)

        list = html.xpath('//span[@property="v:summary"]/text()')
        if len(list) > 0:
            self.description = list[0].strip('\r\n ')

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

    def __getDivInfo__(self, html):
        parent = '//div[@id="info"]'
        self.__getdirector__(html, parent)
        self.__getwriter__(html, parent)
        self.__getactors__(html, parent)
        self.__getType__(html, parent)
        self.__getLocation__(html, parent)
        self.__getLanguage__(html, parent)
        self.__getTime__(html, parent)
        self.__getLength__(html, parent)
        self.__getImdbUrl__(html, parent)

    def __getdirector__(self, html, parent):
        content = html.xpath(parent + '/span[1]/span[@class="attrs"]/a/text()')
        self.director = content

    def __getwriter__(self, html, parent):
        content = html.xpath(parent + '/span[2]/span[@class="attrs"]/a/text()')
        self.writer = content

    def __getactors__(self, html, parent):
        content = html.xpath(parent + '/span[3]/span[@class="attrs"]/span/a/text()')
        self.actors = content

    def __getType__(self, html, parent):
        content = html.xpath(parent + '/span[@property="v:genre"]/text()')
        self.type = content

    def __getLocation__(self, html, parent):
        findLocation = re.compile(r'<span class="pl">制片国家/地区:</span> (.*)<br/>')
        content = html.xpath(parent)
        if len(content) > 0:
            content = etree.tostring(content[0], encoding='utf-8')
            content = content.decode('utf-8')
            content = re.findall(findLocation, content)
            if len(content) > 0:
                self.location = content[0]

    def __getLanguage__(self, html, parent):
        findLanguage = re.compile(r'<span class="pl">语言:</span> (.*)<br/>')
        content = html.xpath(parent)
        if len(content) > 0:
            content = etree.tostring(content[0], encoding='utf-8')
            content = content.decode('utf-8')
            content = re.findall(findLanguage, content)
            if len(content) > 0:
                content = content[0].split(' / ')
                for element in content:
                    self.language.append(element)

    def __getTime__(self, html, parent):
        content = html.xpath(parent + '/span[@property="v:initialReleaseDate"]/text()')
        self.time = content

    def __getLength__(self, html, parent):
        content = html.xpath(parent + '/span[@property="v:runtime"]/text()')
        self.time_length = content

    def __getImdbUrl__(self, html, parent):
        content = html.xpath(parent + '/a/@href')
        if len(content) > 0:
            self.imdbLink = content[0]