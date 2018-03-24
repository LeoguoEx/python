class DBHosts(object):

    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = ''
        self.dbname = 'test'
        self.charset = 'utf8'

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