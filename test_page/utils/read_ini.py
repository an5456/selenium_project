import configparser
import os


class ReadIni:

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            file_name = file + "/data/element.ini"
            print(file_name)
        else:
            self.file_name = file_name

        if node is None:
            self.node = "ContactElement"
        else:
            self.node = node
        self.ele = self.load_ini(file_name)

    def load_ini(self, file_name):
        ele = configparser.ConfigParser()
        ele.read(file_name, encoding='utf-8')
        return ele

    def get_value(self, key):
        data = self.ele.get(self.node, key)
        return data


if __name__ == '__main__':
    s = ReadIni()
    print(s.get_value("add_contact"))
