# phi = float(input("masukkan nilai phi: "))
# jari_jari = float(input("masukkan nilai jari-jari: "))

# volume = phi * (jari_jari**2)
# print("volume adalah: ", volume)

# nama = input("masukkan nama anda: ")
# umur = input("masukkan umur anda: ")
# hobi1 = input("masukkan hobi1 anda: ")
# hobi2 = input("masukkan hobi2 anda: ")

# print("nama saya adalah:", nama)
# print("masukkan umur anda:", umur)
# print("masukkan hobi1 anda:", hobi1)
# print("masukkan hobi2 anda:", hobi2)

# nilai1 = int(input("masukkan bilangan pertama: "))
# nilai2 = int(input("masukkan biilangan kedua:"))

# hasil = nilai1 + nilai2

# print("hasil penjumlahan dari", nilai1, "dan", nilai2, "adalah")
# print(nilai1, "+", nilai2, "=", hasil)

# nama = int(input("masukkan nama: "))

# while nama < 90:
#     print("dia", nama)
#     nama += 1

# nama = input("masukkan nama :")
# usia = int(input("masukkan usia: "))

# tahun_lahir = 2024 - usia

# print("hallo,", nama, "anda lahir pada tahun", tahun_lahir)

# mobil =510
# motor = 20

# hasil = motor + mobil 

# print("jumlah motor dan mobil adalah", hasil)    

# def pesan():
#     print("hallo maniez")
#     print("silahkan duduk")
    
# pesan()

# def hitung_luas_balok(panjang):
#     lebar = 20
#     tinggi = 15
#     luas = panjang * lebar * tinggi
#     return luas

# hasil = hitung_luas_balok(20)
# print("luas balok adalah :", hasil, "cm")

def kuadrat(angka):
    hasil = angka**2
    return hasil

hasil_kuadrat = kuadrat(5)

print("kuadrat dari 5 adalah :", hasil_kuadrat)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

sisi_persegi = float(input("masukkan panjang sisi persegi : "))
hasil_luas_persegi = luas_persegi(sisi_persegi)

alas_segitiga = float(input("masukkan panjang alas segitiga : "))
tinggi_segitiga = float(input("masukkan tinggi segitiga : "))
hasil_luas_segitiga = luas_segitiga(alas_segitiga, tinggi_segitiga)

print("luas persegi adalah:", hasil_luas_persegi)
print("luas segitiga adalah:", hasil_luas_segitiga)

def hitung_total_tiket(jumlah_tiker, harga_tiket):
    total = jumlah_tiket * harga_tiket
    return total

jumlah_tiket = int(input("masukkan jumlah tket yang ingin dibeli: "))
harga_tiket = float(input("masukkan harga per tiket: "))

total_harga = hitung_total_tiket(jumlah_tiket, harga_tiket)

print("total harga untuk", jumlah_tiket, " tiket adalah", total_harga)
    

