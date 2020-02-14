import os

import yaml

from config import base_url


def read_yaml(filename):
    with open(base_url + os.sep + "data" + os.sep + filename, "r", encoding="utf-8") as f:
        arr = []
        for data in yaml.safe_load(f).values():
           arr.append(tuple(data.values()))
        return arr

if __name__ == '__main__':
    print(read_yaml("login.yaml"))