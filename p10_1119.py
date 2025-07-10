import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 35, 30, 25, 40],
        'bebas': [0, 1, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(8, 8)) # Atur ukuran gambar
plt.pie(df['nilai'], labels=df['kategori'], autopct='%1.1f%%', startangle=140)
plt.title('Dagram PAI Nilai per Kategori')
plt.axis('equal')
plt.show()