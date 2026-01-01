import numpy as np
import pandas as pd

dataku = pd.read_csv('data_kapal_titanic.csv') 
print(dataku)
print("\n")
age = dataku[['age']] # mengambil kolom Age
print(age)
print()
print(age.describe()) # untuk menghasilkan statistik deskiriptif dari kolom Age
print("\n")
print(age.count()) # untuk cek seberapa banyak baris data yang tidak kosong
print("\n")

print(20*"=", "membersihkan data", 20*"=")
print(age.agg(['mean', 'median', 'sum', 'std', 'var'])) 
# dalam perhitungan sum atau yang lainnya ketika menggunakan agregate/agg
# si sum ini secara default akan bernilai true skipna nya
# maksud nya adalah ketika penjumlahan seluruh baris data yang kosong
# akan diabaikan, sehingga tidak menghasilkan NaN
# jika ingin menghitung seluruh baris data termasuk yang kosong
# bisa menggunakan skipna=False

age_bersih = age.dropna() # menghapus data yang kosong
print(age_bersih)
print("")
print(age.dropna(subset=['age'])) # menghapus data yang kosong pada kolom age saja
# baris ke 78 tidak digunakan, karena dari awal sudah nge assign kolom age ke variabel age
print("\n")
print(age_bersih.dropna(axis=0, how='any')) # menghapus baris yang ada data kosongnya
print("\n")
print(age_bersih.dropna(thresh=2)) #menghapus baris yang memiliki data kosong kurang dari 2
# menggunakan thresh agar data yang memiliki nilai NaN lebih dari satu tidak dihapus
# karena secara default jika tidak menggunakan thresh, maka akan menghapus baris yang minimal memiliki satu nilai NaN
print("\n")
print(age.info()) # untuk melihat informasi dari kolom Age
print("\n")
dataku2 = dataku.dropna(axis=0, how='any') # menghapus baris yang ada data kosongnya
print(dataku2) # dataku2 sudah bersih dari data yang kosong
print("\n")
# jikka menemukan sebuah data yang kosong, diusahakan untuk tidak menghapusnya
# karena bisa jadi data tersebut penting, hanya karena 1 yang tidak terisi
# untuk antisipasi bisa menggunakan fillna yang dimana nilai yang didapat dari rata rata
#  example:
# dataku.age.fillna(value = dataku2.age.mean())

dataku3 = dataku
print(dataku3)
print()
print("Mengisi data kosong pada kolom age dengan rata-rata")
dataku3.age = dataku3.age.fillna(value=dataku3.age.mean())
print(dataku3.age)
print("")
print("mengubah data dari series ke array")
dataku4 = dataku3.age.values
print(dataku4)
print("")
print("setelah diisi dengan rata-rata")
print(dataku)
print("\n")

# gunakanlah mean hanya untuk data yang numerik