import telnetlib
from IPProxies import IPProxie

class TelnetTest(object):

    def __init__(self):
        pass

    def telnetTest(self, proxie):
        try:
            print('test telnet !!!  ip : %s   port : %s' % (proxie.ip, proxie.port))
            tn = telnetlib.Telnet(proxie.ip, port=proxie.port, timeout=3)
        except:
            return False
        finally:
            return True