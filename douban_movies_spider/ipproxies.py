import random
import datetime

class IpProxies(object):

    def __init__(self):
        self.ipproxies = []
        self.seed = random.seed(datetime.datetime.now())

    def flushIpProxies(self, proxies):
        if proxies is not None:
            self.ipproxies.clear()
            self.ipproxies.extend(proxies)

    def getProxies(self):
        index = random.randint(0, len(self.ipproxies))
        if (index > 0) and (index < len(self.ipproxies)):
            return self.ipproxies[index]
        return ''