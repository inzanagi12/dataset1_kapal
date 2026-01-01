import numpy as np
import pandas as pd

np.random.seed(100)
dataku = pd.DataFrame(np.random.randn(3, 5), ['A', 'B', 'C'], ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima'])
print(dataku)
print("\n")
print(type(dataku['Dua']))
# iloc loc
dataku['baru'] = dataku['Empat'] + dataku['Lima'] #menambahkan kolom baru
print(dataku)
print("\n")
# cara untuk menghapus kolom    
hapus_data = dataku.drop('Tiga',axis=1) #axis 1= untuk kolom, axis= 0 untuk baris
# jika menggunakan inplace=True, maka tidak perlu assign ke variabel baru
# tapi, data akan berubah secara permanen tanpa bisa dikembalikan walaupun di restart
print("Hasil hapus kolom Tiga:")
print(hapus_data)
print("\n")

print("Hasil hapus kolom baru:")
dataku.drop('baru', axis=1, inplace=True) # menghapus kolom baru
# axis 1 untuk kolom, axis=0 untuk baris
hapus_data2 = dataku
print(hapus_data2)
print("perbedaan atas dan bawah")
print(hapus_data) # kolom baru tidak terhapus di hapus_data
print(dataku.shape) # untuk melihat ukuran data atau dimensi data
print(hapus_data2.shape) # untuk melihat ukuran data atau dimensi data
# (baris, kolom)
dataku_bol = dataku < 0 # membuat boolean series
print(dataku_bol) # jika kurang dari 0, maka akan true, jika tidak false
print(dataku[dataku_bol]) # jika bernilai True maka akan NaN, jika False maka akan di tampilkan nilainya

dataku = pd.DataFrame(np.random.randn(3, 5), ['A', 'B', 'C'], ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima'])
print("ceek seluruh baris dan periksa kolomg yang dipilih, sesuai atau tidak dengan aturan")
# semisal contoh pada kode diabawh, mengambil semua data di setiap baris dengan kolom 'Empat' yang lebih besar dari 0
# jika semua baris di kolom 'Empat' lebih besar dari 0, maka akan ditampilkan seluruh barisnya
# jika tidak, maka hanya menampilkan Empty DataFrame
print(dataku[dataku['Empat'] > 0]) # menampilkan semua baris yang kolom Tiga lebih besar dari 0
print(dataku)
dataku['fresh'] = dataku['Empat' ] + dataku['Lima']
print("\n")
print("Menambahkan kolom fresh dengan menjumlahkan kolom Empat dan Lima")
print(dataku)
print(dataku[dataku['Lima'] > 0]) # menampilkan semua baris yang kolom Tiga lebih besar dari 0

