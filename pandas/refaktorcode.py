import pandas as pd
import numpy as np
print(20*"=", "refaktor kode ala ala GPT", 20*"=")
print(20*"=", "eps4C", 20*"=")
# Buat DataFrame contoh
dataku = pd.DataFrame({
    'name': ['Andi', 'Budi', 'Citra', 'Dina', 'Eka'],
    'age': [20, 25, 22, 28, 24],
    'score': [85, 90, 88, 92, 87]
})

# Kalau mau hapus kolom age tanpa bikin error ke baris lain
# Gunakan .drop() dengan errors='ignore' biar aman
# dataku = dataku.drop(columns=['age'], errors='ignore')

# Contoh akses kolom secara aman (tanpa bikin error kalau kolom hilang)
if 'age' in dataku.columns:
    age = dataku['age']
else:
    age = None  # atau pd.Series(dtype='float') biar tipe datanya jelas

# Buat filter boolean untuk score > 87
dataku_bol = dataku['score'] > 87

# Cetak hasil filter
print("Data dengan score > 87:")
print(dataku[dataku_bol])
