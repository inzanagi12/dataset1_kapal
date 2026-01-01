# masukkan_angka = int(input("masukkan nilai : "))

# if masukkan_angka == 0:
#     print("0 bukanlah bilangan genap ganjil")
# elif masukkan_angka % 2 == 0:
#     print("merupakan bilangan genap")
# else:
#     print("merupakan bilangan ganjil")

Nama = (input("masukkan nama : "))
NPM = (input("masukkan NPM : "))
Kelas = (input("masukkan kelas : "))
mata_kuliah = (input("masukkan matkul : "))

uts = int(input("masukkan nilai uts : "))
uas = int(input("masukkan nilai uas : "))
hasil = (uts * 50/100) + (uas * 50/100)

if (hasil < 100):
    print("mendapatkan nilai A")
elif (hasil < 86):
    print("mendapatkan nilai B")
elif (hasil < 70):
    print("mendapatkan nilai C")
else:
    print("mendapatkan nilai D")
    
print("hallo nama saya", Nama, "NPM saya", NPM, "berada di kelas", Kelas, "dan ber mata kuliah", mata_kuliah, "yang memiliiki nilai uts dan uas adalah", hasil)