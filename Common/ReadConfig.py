import configparser
import os


class ReadConf:

    def __init__(self, section, option):
        self.config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Config\\Conf.ini")
        self.section = section
        self.option = option

    def read_db(self):
        config = configparser.ConfigParser()
        config.read(self.config_path, encoding="utf-8")
        all_sections = config.get(self.section, self.option)
        return all_sections
