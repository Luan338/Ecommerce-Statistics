# Library Imports: pandas, numpy, matplotlib, seaborn
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;

# Import Data Source: Ecommerce Statistics.csv
df = pd.read_csv('ecommerce_estatistica.csv');

# 01) Data Reading and Cleaning
print("-" * 50);
print('Initial view of the data (head):');
print(df.head());
print('\n');

print('Dataframe Information (info):');
print(df.info());
print('\n');

print('Count missing values by column:');
print(df.isnull().sum());
print('\n');

print(f"\nDataFrame {df.shape[0]} lines and {df.shape[1]} columns.")
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# 02) Detailed Analysis
print("-" * 50);
print("Descriptive Analysis of Numerical Columns:\n");
print(df[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].describe());
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 01 (Histogram): Distribution of product scores
print("-" * 50);

color_yellow = '#FFD60A';
color_blue = '#33A1F2';
color_gray = '#F3F4F6';
color_title = '#211A1A';

counts, bins, _ = plt.hist(df['Nota'], bins=10);

cmap = plt.cm.get_cmap('YlOrRd');
cores = cmap(counts / max(counts));

plt.figure(figsize=(10, 6));
plt.bar(bins[:-1], counts, width=np.diff(bins), color=cores, edgecolor='black', alpha=0.8);
plt.title('Product Rating Distribution', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Nota', fontsize=12);
plt.ylabel('Frequency', fontsize=12);
plt.grid(axis='y', linestyle='--', alpha=0.6);

ax2 = plt.twinx()
sns.kdeplot(df['Nota'], color=color_blue, lw=2);

plt.show();
print("The graph above shows the distribution of product scores, indicating which score ranges are most common among items.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 02 (Bar Chart): TOP 10 brands by quantity sold
map = {
    '+10mil': 10000,
    '+50mil': 50000,
    '+1000': 1000,
    '+100': 100,
    '+50': 50,
    '+5': 5,
    '+25': 25
}
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].replace(map)
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(int)

marcas_mais_vendidas = df.groupby('Marca')['Qtd_Vendidos'].sum().nlargest(10).sort_values(ascending=False)

cores_barras = cmap(marcas_mais_vendidas.values / marcas_mais_vendidas.values.max())

plt.figure(figsize=(12, 7))

sns.barplot(x=marcas_mais_vendidas.values, y=marcas_mais_vendidas.index, palette=cores_barras)

plt.title('Top 10 Best-Selling Brands', fontsize=20, fontweight='bold', color=color_title)
plt.xlabel('Quantity Sold', fontsize=12)
plt.ylabel('Mark', fontsize=12)

for index, value in enumerate(marcas_mais_vendidas.values):
    plt.text(value, index, f' {value}', va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.6)
sns.despine(left=True, bottom=True)

plt.show()

print("The graph above visualizes the 10 brands with the highest sales volume, highlighting each brand's market leadership, using the same color scheme as the distribution graph.")
print("-" * 50)
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 03:
