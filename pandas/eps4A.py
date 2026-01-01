import pandas as pd
import numpy as np

label = ['satu', 'dua', 'tiga']
angka = [10, 20, 30]
np_angka = np.array(angka)
print(np_angka) # di index tidak ada index tertulis seperti di pandas
print("\n")
d = {'satu':10, 'dua':20, 'tiga':30}
print(pd.Series(data=angka)) #di pandas secara eksplisit ada index nya
print(pd.Series(data=angka, index=label)) #index bisa ditentukan
print(pd.Series(data=np_angka, index=label)) #index bisa ditentukan
print(pd.Series(data=angka, index=label, name='angka banding 10'))
dataku = pd.Series(data=angka, index=label, name='angka banding 10') #index bisa ditentukan dan ada nama kolomnya buat judul
print(dataku['satu'])

dataSet = pd.Series(d, index=label, name='panjang data')
print(dataSet)
print(pd.Series(np_angka))
# panjang kedua data diatas itu sama, yaitu 64. namun jika ingin mengubahnya ke 32
# bisa menggunakan dtype=np.int32
data_baru = np.array(angka, dtype=np.int32)
s= pd.Series(data=data_baru, index=label, name='perubahan panjang data')
print(s)
print("\n")
data_baru2 = dataku.to_frame() # mengubah series menjadi dataframe
print(data_baru2)
data_baru2.info()
print("\n")
d2 = {'satu':10, 'dua':20, 'tiga':30, 'empat':40, 'lima':50}
dataku = pd.Series(d)
dataku2 = pd.Series(d2)

print(dataku)
print("\n")
print(dataku2)
penjumlahan = dataku + dataku2 # penjumlahan series
print(penjumlahan) #sesama series bisa dijumlahkan asaalkan indexnya sama
# jika tidak sama, maka akan menghasilkan NaN pada index yang tidak ada


