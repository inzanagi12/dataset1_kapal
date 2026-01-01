import pandas as pd
dataku = pd.read_csv('kapal_titanic.csv')
dataku.info()
print(type(dataku))

print("penjelasan pada tahap pertama")
print(dataku)
data_baru = dataku['age']
print("\n", data_baru)
data_baru = dataku['age'].agg(['mean', 'max', 'min']) #aggregate function
print("\n", data_baru)
data_baru = dataku['age'].agg(['mean', 'max', 'min']).to_frame() #convert to dataframe
print("\n", data_baru)
data_baru = dataku[['age', 'fare']].agg(['mean', 'max', 'min']) #multiple columns
print("\n", data_baru)

print("\n", "penjelasan pada tahap kedua: DOT NOTATIONS")
data_baru = dataku.age.agg(['mean', 'max', 'min']) #using dot notation
print("\n", data_baru)

print("\n", "penjelasan pada tahap ketiga: .ILOC")
# .iloc untuk mengambil data berdasarkan index atau posisi atau int
data_baru = dataku.iloc[0:11] # mengambil 11 data teratas
print("\n", data_baru)
data_baru = dataku.iloc[:, 3] # mengambil semua baris dan kolom ke 3 saja
print("\n", data_baru)
data_baru = dataku.iloc[-5:-1, -4:-2] #ambil 5 baris terakhir kecuali baris terakhir, dan kolom dari -4 ke -2
print("\n", data_baru)
data_baru = dataku.iloc[[0,2,4], [1,3,6]] # spesifikasi pemilihan baris dan kolom
print("\n", data_baru)

print("\n", "oenjelasan pada tahap keempat: .LOC")
# .loc['label', 'label']
data_data = pd.read_csv('kapal_titanic.csv', index_col='embarked')
print("\n", data_data)
print("\n", data_data.index.unique)
data_baru = data_data.loc['S', 'age']
print("\n", data_baru)
data_baru = data_data.loc[['S', 'C'], 'age'].agg(['mean', 'max', 'min'])
print("\n", data_baru)
data_baru = data_data.loc[['S', 'C'], 'age']
print("\n",data_baru)