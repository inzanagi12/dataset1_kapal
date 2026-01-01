def menentukanBilanganGanjil():
    angka = int(input("Masukkan angka: "))
    if(angka % 2 == 1):
        print(f"angka {angka} merupakan bilangan ganjil")
    else:
        print(f"angka {angka} merupakan bilangan genap")
        
menentukanBilanganGanjil()
print("\n")
angka = [1,2,3,4,5]
print(angka)
angka_kuadrat = list(map(lambda x: x**2, angka))
print(angka_kuadrat)