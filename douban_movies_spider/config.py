import json
import os
from ConfigStruct.DBHosts import DBHosts

class Config(object):

    PATH_PREFIX = 'Json/{0}.json'

    def __init__(self):
        self.dict = {'DBHosts' : None}
        self.__initData__()
        self.__initFile__()
        self.__getFileData__()

    def getData(self, name):
        if self.dict.__contains__(name):
            return self.dict[name]
        return None

    def __initData__(self):
        for key in self.dict.keys():
            confClass = eval('{0}()'.format(key))
            self.dict[key] = confClass

    def __initFile__(self):
        for key in self.dict.keys():
            path = self.PATH_PREFIX.format(key)
            if os.path.exists(path) is not True:
                with open(path, 'w+') as f:
                    data = self.dict[key]
                    json.dump(data.getDict(), f)
                    f.close()

    def __getFileData__(self):
        for key in self.dict.keys():
            path = self.PATH_PREFIX.format(key)
            with open(path, 'r', encoding='utf-8') as f:
                dic = json.load(f)
                self.dict[key].setDict(dic)
                f.close()


