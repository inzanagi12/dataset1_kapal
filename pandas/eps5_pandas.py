import pandas as pd
import matplotlib.pyplot as plt

dataku = pd.read_csv('kapal_titanic.csv')
print(dataku)
# print(dataku['age'].hist())
# plt.show()
# print(dataku['age'].hist(bins=5))
# plt.show()
# #  di dalam vscode, untuk menampilkan grafik, selalu gunakan ply.show()
# print(dataku['age'].hist(bins=5, color='red', alpha=0.1))
# plt.show()
# print(dataku['age'].hist(bins=5, color='red', alpha=0.5, edgecolor='black'))
# plt.show()

import seaborn as sns
sns.set(style='whitegrid', palette='muted', font_scale=1.2, rc={'figure.figsize': (10, 6)})
print(dataku.age.plot.hist(bins=30, alpha=0.4))
plt.show()
# dalam menggunakan seaborn, kita bisa menggunakan fungsi sns.set() untuk mengatur tema grafik
# sns.set() akan mengatur tema grafik menjadi lebih menarik dan mudah dibaca

