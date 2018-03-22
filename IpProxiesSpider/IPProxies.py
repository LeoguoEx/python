from lxml import etree
import re

class IPProxie(object):

    def __init__(self, ip, port, protocol, speed, connect_time):
        self.ip = ''.join(ip)
        self.port = ''.join(port)
        self.protocol = ''.join(protocol)
        self.speed = speed
        self.connect_time = connect_time

    def printProxie(self):
        print("ip=%s   port=%s   protocol=%s   speed=%d   connect_time=%d" % (self.ip, self.port, self.protocol, self.speed, self.connect_time))

    @staticmethod
    def parse(html):
        content = etree.HTML(html)
        body_list = content.xpath('//table[@id="ip_list"]//tr')
        proxies_list = []
        if body_list is not None:
            first = False
            for body in body_list:
                if first is not True:
                    first = True
                    continue
                proxies = IPProxie.__parseBody__(body)
                if proxies is not None:
                    proxies_list.append(proxies)
        return proxies_list

    @staticmethod
    def __parseBody__(body):
        ip = body.xpath('.//td[2]/text()')
        port = body.xpath('.//td[3]/text()')
        protocol = body.xpath('.//td[6]/text()')
        speed = int(IPProxie.__parseSlider__(body.xpath('.//td[7]/div/div')))
        connect_time = int(IPProxie.__parseSlider__(body.xpath('.//td[8]/div/div')))
        data = IPProxie(ip, port, protocol, speed, connect_time)
        return data

    @staticmethod
    def __parseSlider__(slider):
        if slider is None or len(slider) == 0:
            return None

        text = etree.tostring(slider[0], encoding='utf-8')
        text = text.decode('utf-8')
        pattern = re.compile('style="width:(.*)%"')
        content = re.findall(pattern, text)
        if len(content) > 0:
            return content[0]
        return None
