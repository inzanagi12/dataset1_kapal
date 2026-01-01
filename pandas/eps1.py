import os
import pandas as pd

print(os.getcwd())
data = pd.read_csv('kapal_titanic.csv')
print("data asli")
print(data)
print("\n10 data teratas")
print(data.head(10))
print("\n10 data terbawah")
print(data.tail(10))

print("\nimport data") #dari csv ke csv lain
data.to_csv('data_kapal_titanic.csv', index=False)
print(pd.read_csv('data_kapal_titanic.csv'))

print("\nexport data") # dari csv ke excel
data.to_excel('data_kapal_titanic.xlsx', index=False, sheet_name='sheet manja')
print(pd.read_excel('data_kapal_titanic.xlsx', sheet_name='sheet manja'))
print("\nimport data dari html")
datahtml = pd.read_html('https://www.fdic.gov/bank-failures/failed-bank-list')
print(datahtml[0])

print("SQL Alchemy")
from sqlalchemy import create_engine
mesin = create_engine('sqlite:///:memory:')
data.to_sql('datasql', con=mesin, index=False, if_exists='replace')
pd.read_sql('datasql', con=mesin)