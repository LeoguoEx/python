#一些静态数据的存储，解析配置文件

import csv

class ConfigManager:

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        pass

    def initFileHeader(self):
        pass