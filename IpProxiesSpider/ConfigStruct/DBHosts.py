
class DBHosts(object):

    def __init__(self):
        self.host = None
        self.port = None
        self.user = None
        self.password = None
        self.dbname = None
        self.charset = None

    def getDict(self):
        dic = {"host" : self.host,
               "port" : self.port,
               "user" : self.user,
               "password": self.password,
               "dbname" : self.dbname,
               "charset" : self.charset}
        return dic

    def setDict(self, dic):
        if dic is None:
            return False
        self.host = dic["host"]
        self.port = dic["port"]
        self.user = dic["user"]
        self.password = dic["password"]
        self.dbname = dic["dbname"]
        self.charset = dic["charset"]
        return True