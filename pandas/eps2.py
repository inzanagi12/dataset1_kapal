import pandas as pd
dataku = pd.read_csv('kapal_titanic.csv')
print("melihat banyaknya kolom")
pd.options.display.max_columns = 890  #untuk menampilkan semua kolom, harus nge assgin total kolom yang ada
print(pd.options.display.max_columns)
print("\nmelihat sedikitnya baris dari yang ditampilkan")
pd.options.display.max_rows = 890 #begitupun juga untuk menampilkan semua baris
print(pd.options.display.max_rows)
print("\ndata asli")
dataku.info()
print("\n", dataku)
print("\n ringkasan data statistik")
print(dataku.describe())  #untuk melihat ringkasan statistik dari data
print("\n data yang bukan numerik")
print(dataku.describe(include = 'object'))  #untuk melihat ringkasan statistik dari data yang kolom bertipe object
print("\n semua data")
print(dataku.describe(include = 'all'))  #untuk melihat ringkasan statistik dari semua kolom
print("\n kolom numerik")
print(dataku.describe(include = 'number'))  #untuk melihat ringkasan statistik dari data yang numerik
try:
    print("\n kolom kategori")
    print(dataku.describe(include = 'category'))  #untuk melihat ringkasan statistik dari data kolom kategori
except Exception as e:
    print("Kolom kategori tidak ditemukan:", e)
