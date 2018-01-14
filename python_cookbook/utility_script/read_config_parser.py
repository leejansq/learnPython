# -*-coding:utf-8-*-

from configparser import ConfigParser

cfg = ConfigParser()
raw_config = cfg.read("config.ini")
sections = cfg.sections()
library = cfg.get('installation', 'library')

print(library)
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.get('server', 'signature'))


cfg.set('server','port','9000')

