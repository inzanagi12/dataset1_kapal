print(20*"=", "eps 2", 20*"=")
import numpy as np

# memebuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5, 6, 7])

# membuat vector dengan range
c = np.arange(1,10,2) #membuat range dari 1 sampe 10 dengan longkap 2

# membuat linspace 
d = np.linspace(1, 10, 4) # membuat range dari 1 sampe 10 dengan isi 4 angka yang seimbang

# array multidimensi / matrix
e = np.array([(1,2,3) , (4,5,6)]) #array 2 dimensi

# matrix dengan nilai nol
f = np.zeros((5,5))

# meatrix dengan nilai satu
g = np.ones((5,5))

# matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

# display
print(f)

print(20*"=", "eps 3", 20*"=")
# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTWISE operation
# penjumlahan
hasil = anp + bnp

# pengurangan
hasil = anp - bnp

# perkalian
hasil = anp * bnp

# pembagian
hasil = anp / bnp

# kuadrat
hasil = anp**2

# multidimensi array numpy
c = np.array(([1,2,3], [4,5,6]))
d = np.array(([7,8,9], [-1,-2,-3]))

hasil = c + d
hasil = c * d
print(hasil)

print(20*"=", "eps 4", 20*"=")


