from lxml import etree
import re

class IPProxie(object):

    ipproxies = {}

    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    @staticmethod
    def parse(html):
        content = etree.HTML(html)
        body_list = content.xpath('//tbody/tr')

        proxies_dic = []
        if body_list is not None:
            for body in body_list:
                proxie = IPProxie.parseBody(body)
                if proxie is not None:
                    proxies_dic.append(proxie)

        return proxies_dic

    @staticmethod
    def __parseBody__(body):
        ip = body.xpath('/td[1]/text()')
        port = body.xpath('/td[2]/text()')
        protocol = body.xpath('/td[5]/text()')
        speed = IPProxie.parseSlider(body.xpath('/td[6]'))
        connect_time = IPProxie.parseSlider(body.xpath('/td[7]'))

        if speed >= 80 and connect_time >= 90:
            proxie = IPProxie(ip, port, protocol)
            return proxie
        return None





    @staticmethod
    def __parseSlider__(slider):
        text = slider.xpath('text()')
        pattern = re.compile('style="width:(.*)%"')
        content = re.findall(text, pattern)
        if len(content) > 0:
            return content[0]
        return None
