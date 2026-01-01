import pandas as pd

satu = pd.DataFrame({'A': ['a0', 'a1', 'a2', 'a3', 'a4', 'a5'],
                     'B': ['b0', 'b1', 'b2', 'b3', 'b4', 'b5'],
                     'C': ['c0', 'c1', 'c2', 'c3', 'c4', 'c5'],
                     'D': ['d0', 'd1', 'd2', 'd3', 'd4', 'd5']},
                    index=[0, 1, 2, 3, 4, 5])

dua = pd.DataFrame({'A': ['a6', 'a7', 'a8', 'a9', 'a10', 'a11'],
                     'B': ['b6', 'b7', 'b8', 'b9', 'b10', 'b11'],
                     'C': ['c6', 'c7', 'c8', 'c9', 'c10', 'c11'],
                     'D': ['d6', 'd7', 'd8', 'd9', 'd10', 'd11']},
                    index=[6, 7, 8, 9, 10, 11])

tiga = pd.DataFrame({'A': ['a12', 'a13', 'a14', 'a15', 'a16', 'a17'],
                     'B': ['b12', 'b13', 'b14', 'b15', 'b16', 'b17'],
                     'C': ['c12', 'c13', 'c14', 'c15', 'c16', 'c17'],
                     'D': ['d12', 'd13', 'd14', 'd15', 'd16', 'd17']},
                    index=[12, 13, 14, 15, 16, 17]) 

print(satu)
print(dua)
print(tiga)

# concatenatenation
print("\nConcatenation")
gabung = pd.concat([satu, dua, tiga], axis=0) # axis 0 = baris, axis 1 = kolom
print(gabung)
# karena axis dia 0, maka dia akan sejajar dengan kolomnya, ditandai dengan kolom A, B, C, D yang sama
# jika axis dia 1, maka dia akan menyesuaikan dengan barisnya, ditandai dengan index yang sama
# jika ada yang tidak sesuai, maka akan diisi dengan NaN


bisnis = pd.DataFrame({'perusahaan' : ['pertamina', 'indosat', 'telkomsel', 'bri', 'pertamina', 'telkomsel', 'KFC', 'KFC'],
                       'karyawan' : ['andi', 'budi', 'caca', 'dodi', 'erik', 'fafa', 'gaga', 'hahi'],
                       'usia': [23, 25, 27, 22, 24, 26, 21, 23]})
print("\nBisnis")
print(bisnis)

print(bisnis.groupby('perusahaan'))
# jika ingin menghitung mean/sum satu kolom saja bisa menggunakan ['nama_kolom']
print(bisnis.groupby('perusahaan')['usia'].mean()) # mean = rata-rata
# jika ingin menghitung kolom numerik saja, bisa menggunakan parameter numeric_only=True
print(bisnis.groupby('perusahaan').sum(numeric_only=True)) # sum = jumlah
# kalau ingin menghitung jumlah data, bisa menggunakan count()
print(bisnis.groupby('perusahaan').count()) # count = menghitung