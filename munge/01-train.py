#!/usr/bin/python3
"""

Complete!
"""
import pandas as pd
import zipfile


FILE_PATH = './data/original/'


def load_data(path, name):
    z = zipfile.ZipFile(path + name + '.zip')
    return pd.read_csv(z.open(name))


if __name__ == '__main__':
    print("Started!")
    train = load_data(FILE_PATH, 'train.csv')
    train.to_csv('./data/prepped/' + 'train.csv', index=False)
    print("Finished!")
