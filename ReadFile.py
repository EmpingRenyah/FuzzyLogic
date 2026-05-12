import pandas as pd

def readExcel() -> pd.DataFrame:
    df = pd.read_excel('restoran.xlsx')
    return df