import telnetlib
from IPProxies import IPProxie

class TelnetTest(object):

    def __init__(self):
        pass

    def telnetTest(self, proxie):
        try:
            tn = telnetlib.Telnet(proxie.ip, port=proxie.port, timeout=10)
        except:
            return False
        finally:
            return True