#!/usr/bin/python3
"""

Not Complete!
"""
import math
import numpy as np
import pandas as pd
import zipfile


FILE_PATH = './data/original/'


def load_data(path, name):
    z = zipfile.ZipFile(path + name + '.zip')
    return pd.read_csv(z.open(name))


# A function to calculate Root Mean Squared Logarithmic Error (RMSLE)
# https://www.kaggle.com/marknagelberg/caterpillar-tube-pricing/rmsle-function
def rmsle(y, y_pred):
    assert len(y) == len(y_pred)
    terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i, pred in enumerate(y_pred)]
    return (sum(terms_to_sum) * (1.0/len(y))) ** 0.5


if __name__ == '__main__':
    print("Started!")
    cliente_tabla = load_data(FILE_PATH, 'cliente_tabla.csv')
    producto_table = load_data(FILE_PATH, 'producto_tabla.csv')
    test = load_data(FILE_PATH, 'test.csv')
    town_state = load_data(FILE_PATH, 'town_state.csv')
    train = load_data(FILE_PATH, 'train.csv')
    print("Finished!")
