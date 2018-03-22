import json
import os
from ConfigStruct.DBHosts import DBHosts

class Config(object):

    DB_HOSTS_PATH = 'Json/db_hosts.json'

    def __init__(self):
        self.initDBHostsFile()
        self.dbhosts = self.__getDBHosts__()

    def initDBHostsFile(self):
        dic = {'host':'localhost', 'port':3306, 'user':'root', 'password':'', 'dbname':'test', 'charset':'utf8'}
        host = DBHosts()
        host.setDict(dic)
        if os.path.exists(self.DB_HOSTS_PATH) is not True:
            with open(self.DB_HOSTS_PATH, 'w+') as f:
                json.dump(host.getDict(), f)
                f.close()

    def __getDBHosts__(self):
        try:
            with open(self.DB_HOSTS_PATH, 'r', encoding='utf-8') as f:
                dic = json.load(f)
                data = DBHosts()
                data.setDict(dic)
                f.close()
        finally:
            return data