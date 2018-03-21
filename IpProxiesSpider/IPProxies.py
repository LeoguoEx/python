from lxml import etree
import re

class IPProxie(object):

    ipproxies = {}

    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def printProxie(self):
        print("ip='%s'   port='%s'" % (self.ip, self.port))

    @staticmethod
    def parse(html):
        content = etree.HTML(html)
        body_list = content.xpath('//table[@id="ip_list"]//tr')
        proxies_list = []
        if body_list is not None:
            for index in range(1, len(body_list) - 1):
                proxie = IPProxie.__parseBody__(body_list[index])
                if proxie is not None:
                    proxies_list.append(proxie)
        return proxies_list

    @staticmethod
    def __parseBody__(body):
        print(etree.tostring(body))
        print(etree.tostring(body.xpath('/td[1]')))
        ip = body.xpath('/td[1]/text()')
        port = body.xpath('/td[2]/text()')
        protocol = body.xpath('/td[5]/text()')
        speed = IPProxie.__parseSlider__(body.xpath('/td[6]/text()'))
        connect_time = IPProxie.__parseSlider__(body.xpath('/td[7]/text()'))

        if speed >= 80 and connect_time >= 90:
            proxie = IPProxie(ip, port, protocol)
            return proxie
        return None

    @staticmethod
    def __parseSlider__(slider):
        text = slider
        pattern = re.compile('style="width:(.*)%"')
        content = re.findall(text, pattern)
        if len(content) > 0:
            return content[0]
        return None
