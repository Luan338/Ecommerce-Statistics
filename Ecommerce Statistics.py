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

# Data cleaning step for the 'Qtd_Vendidos' column, as it contains non-numeric values
map_qtd_vendidos = {
    '+10mil': 10000,
    '+50mil': 50000,
    '+1000': 1000,
    '+100': 100,
    '+50': 50,
    '+5': 5,
    '+25': 25
}
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].replace(map_qtd_vendidos)
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(int)

# 02) Detailed Analysis (Descriptive)
print("--- Detailed Analysis ---")
print("Descriptive Analysis of Numerical Columns:\n");
print(df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos']].describe().T);
print("-" * 50);

# Define color palette for consistency
color_yellow = '#FFD60A';
color_blue = '#33A1F2';
color_title = '#211A1A';
cmap = plt.cm.get_cmap('YlOrRd');

# Graphic 01 (Histogram): Distribution of product scores
print("--- Graphic 01: Product Rating Distribution ---");

counts, bins, _ = plt.hist(df['Nota'], bins=10);
cores = cmap(counts / counts.max());

plt.figure(figsize=(10, 6));
plt.bar(bins[:-1], counts, width=np.diff(bins), color=cores, edgecolor='black', alpha=0.8);
plt.title('Product Rating Distribution', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Rating', fontsize=12);
plt.ylabel('Frequency', fontsize=12);
plt.grid(axis='y', linestyle='--', alpha=0.6);

ax2 = plt.twinx()
sns.kdeplot(df['Nota'], ax=ax2, color=color_blue, lw=2);
ax2.set_ylim(0, max(counts) * 1.1 / len(df['Nota']))
ax2.set_yticks([])
sns.despine(right=True)

plt.show();
print("The graph above shows the distribution of product scores, indicating which score ranges are most common among items.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 02 (Bar Chart): TOP 10 brands by quantity sold
print("--- Graphic 02: Top 10 Best-Selling Brands ---");

marcas_mais_vendidas = df.groupby('Marca')['Qtd_Vendidos'].sum().nlargest(10).sort_values(ascending=False);
cores_barras = cmap(marcas_mais_vendidas.values / marcas_mais_vendidas.values.max());

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
print("The graph above visualizes the 10 brands with the highest sales volume, highlighting each brand's market leadership.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 03 (Scatter Plot): Relationship between price and quantity sold
print("--- Graphic 03: Relationship between Price and Quantity Sold ---");

plt.figure(figsize=(10, 6));
sns.scatterplot(data=df, x='Preço', y='Qtd_Vendidos', hue='Nota', size='Nota', palette='YlOrRd', sizes=(20, 200));
plt.title('Relationship between Price, Quantity Sold, and Rating', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Price', fontsize=12);
plt.ylabel('Quantity Sold', fontsize=12);
plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("This scatter plot visualizes the relationship between the price and the quantity sold, with the points colored and sized according to the product's rating.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 04 (Heatmap): Correlation matrix of numerical variables
print("--- Graphic 04: Correlation Matrix Heatmap ---");

numerical_cols = ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos'];
correlation_matrix = df[numerical_cols].corr();

plt.figure(figsize=(10, 8));
sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", linewidths=.5);
plt.title('Correlation Matrix of Numerical Variables', fontsize=16, fontweight='bold', color=color_title);

plt.show();
print("This heatmap shows the correlation coefficients between numerical variables. Values closer to 1 or -1 indicate a strong positive or negative relationship, respectively.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 05 (Pie Chart): Distribution of products by gender
print("--- Graphic 05: Product Distribution by Gender ---");

gender_counts = df['Gênero'].value_counts();

plt.figure(figsize=(8, 8));
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'));
plt.title('Product Distribution by Gender', fontsize=16, fontweight='bold', color=color_title);

plt.show();
print("This pie chart illustrates the proportion of products for each gender category.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 06 (Regression Plot): Price vs. Quantity Sold with Regression Line
print("--- Graphic 06: Regression Plot of Price vs. Quantity Sold ---");

plt.figure(figsize=(10, 6));
sns.regplot(data=df, x='Preço', y='Qtd_Vendidos', line_kws={'color': 'red'});
plt.title('Regression Plot: Price vs. Quantity Sold', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Price', fontsize=12);
plt.ylabel('Quantity Sold', fontsize=12);
plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("This regression plot shows the linear relationship between the product price and the quantity sold, with the red line indicating the trend.");
print("-" * 50);

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 07 (Density Plot): Price Density Distribution
print("--- Graphic 07: Price Density Distribution ---");

plt.figure(figsize=(10, 6));
sns.kdeplot(df['Preço'], shade=True, color=color_blue, linewidth=2);
plt.title('Price Density Distribution', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Price', fontsize=12);
plt.ylabel('Density', fontsize=12);
plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("This density plot provides a smooth visualization of the distribution of product prices.");
print("-" * 50);