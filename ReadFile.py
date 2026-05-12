import pandas as pd

def readExcel():
    df = pd.read_excel('restoran.xlsx')
    print(df)