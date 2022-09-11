import csv
import pandas as pd

def load_csv():
    print('check csv 4')
    df = pd.read_csv('./tmpdownloads/addresses.csv')

    print(df)

    return 'success'