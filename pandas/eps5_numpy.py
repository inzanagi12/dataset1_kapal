import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

angka = []
for i in range(0, 100):
    angka.append(i)
    
baru = pd.DataFrame(np.random.rand(100,5), angka,['a','b','c','d','e'])
# jika ingin mendapatkan angka negatif di random, maka di bagian rand di tambahkan s
baru.head()

baru.plot.area()
plt.show()

baru2 = pd.DataFrame(np.random.rand(4,5), [0,1,2,3], ['A','B','C','D','E'])
baru2.plot.area()
plt.show()

baru2.plot.bar()
plt.show()

baru2.plot.bar(stacked=True)
plt.show()

baru2['C'].plot.bar(stacked=True)
plt.show()

baru2.plot.scatter(x='A', y='B', c='C', s=baru2['D']*100, alpha=0.5)


