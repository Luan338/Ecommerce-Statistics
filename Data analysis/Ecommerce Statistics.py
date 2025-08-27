# Library Imports: pandas, numpy, matplotlib, seaborn
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Import Data Source: Ecommerce Statistics.csv
df = pd.read_csv('../Database/ecommerce_estatistica.csv');
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Data Reading and Cleaning
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
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Detailed Analysis (Descriptive)
print("--- Detailed Analysis ---")
print("Descriptive Analysis of Numerical Columns:\n");
print(df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos']].describe().T);
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Define color palette for consistency
color_yellow = '#FFD60A';
color_blue = '#33A1F2';
color_title = '#211A1A';
cmap = plt.cm.get_cmap('YlOrRd');
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 01 (Histogram): Distribution of product scores
print("--- Graphic 01: Product Rating Distribution ---");

counts, bins, _ = plt.hist(df['Nota'], bins=10, density=True);

cores = cmap(counts / counts.max());

plt.figure(figsize=(10, 6));

plt.bar(bins[:-1], counts, width=np.diff(bins), color=cores, edgecolor='black', alpha=0.8);

sns.kdeplot(df['Nota'], color=color_blue, lw=2);

plt.title('Distribuição das notas dos produtos', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Notas', fontsize=12);
plt.ylabel('Density', fontsize=12);
plt.grid(axis='y', linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("O gráfico acima mostra a distribuição das notas dos produtos, indicando quais faixas de pontuação são mais comuns entre os itens.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 02 (Bar Chart): TOP 10 brands by quantity sold
print("--- Graphic 02: Top 10 Best-Selling Brands ---");

marcas_mais_vendidas = df.groupby('Marca')['Qtd_Vendidos'].sum().nlargest(10).sort_values(ascending=False);
cores_barras = cmap(marcas_mais_vendidas.values / marcas_mais_vendidas.values.max());

plt.figure(figsize=(12, 7))
sns.barplot(x=marcas_mais_vendidas.values, y=marcas_mais_vendidas.index, palette=cores_barras)

plt.title('TOP 10 marcas mais vendidas', fontsize=20, fontweight='bold', color=color_title)
plt.xlabel('Quantidade Vendida', fontsize=16)
plt.ylabel('Marca', fontsize=12)

for index, value in enumerate(marcas_mais_vendidas.values):
    if value >= 1000:
        plt.text(value, index, f' {value/1000:.0f}k', va='center', fontsize=10)
    else:
        plt.text(value, index, f' {value}', va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.6)
sns.despine(left=True, bottom=True)

plt.show()
print("The graph above visualizes the 10 brands with the highest sales volume, highlighting each brand's market leadership.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 03 (Combined Plot): Relationship between price and quantity sold with density
print("--- Graphic 03: Relationship between Price and Quantity Sold (with Density) ---");

df_filtrado = df[df['Qtd_Vendidos'] <= 10000]

plt.figure(figsize=(12, 8));

sns.scatterplot(data=df_filtrado, x='Preço', y='Qtd_Vendidos', hue='Nota', size='Nota', palette='YlOrRd', sizes=(20, 200), alpha=0.7);

sns.kdeplot(data=df_filtrado, x='Preço', y='Qtd_Vendidos', cmap="Blues", fill=True, alpha=0.5, thresh=0.1);

plt.title('Relação entre Preço, Quantidade Vendida e Nota com Agrupamento de Dados', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Preço', fontsize=12);
plt.ylabel('Quantidade Vendida', fontsize=12);

plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("O gráfico de dispersão acima agora combina a visualização dos pontos com uma camada de densidade (áreas azuis). As áreas azuis mais escuras indicam onde os dados estão mais agrupados, respondendo à sua pergunta sobre como visualizar a densidade dos pontos.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 04 (Heatmap): Correlation matrix of numerical variables
print("--- Graphic 04: Correlation Matrix Heatmap ---");

numerical_cols = ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos'];
correlation_matrix = df[numerical_cols].corr();

plt.figure(figsize=(10, 8));
sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", linewidths=.5);
plt.title('Matrix de Correlação das variáveis numéricas', fontsize=16, fontweight='bold', color=color_title);

plt.show();
print("Este mapa de calor mostra os coeficientes de correlação entre variáveis numéricas. Valores próximos de 1 ou -1 indicam uma forte relação positiva ou negativa, respectivamente.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 05 (Pie Chart): Distribution of products by gender
print("--- Graphic 05: Product Distribution by Gender ---");

color_title = '#211A1A';
cmap = plt.cm.get_cmap('YlOrRd');

gender_counts = df['Gênero'].value_counts();
total_produtos = gender_counts.sum();

percent_limite = 0.014;
gender_counts_filtrado = gender_counts[gender_counts / total_produtos > percent_limite];

outros = total_produtos - gender_counts_filtrado.sum();

gender_counts_filtrado['Outros'] = outros;

gender_counts_ordenado = gender_counts_filtrado.sort_values(ascending=True);

cores_fatias = cmap(gender_counts_ordenado.values / gender_counts_ordenado.values.max());

plt.figure(figsize=(8, 8));

plt.pie(gender_counts_ordenado, labels=gender_counts_ordenado.index, autopct='%1.1f%%', startangle=140, colors=cores_fatias, wedgeprops={'edgecolor': 'black'});

plt.title('Distribuição de Produtos por Gênero', fontsize=16, fontweight='bold', color=color_title);
plt.axis('equal');

plt.show();
print("O gráfico mostra as categorias com mais de 1.4%, agrupando as demais em 'Outros', e as cores são baseadas na quantidade vendida para cada gênero.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 06: Regression Plot of Nota vs. Quantity Sold (Normalized)
print("--- Graphic 06: Regression Plot: Nota vs Quantity Sold (Normalized) ---");

df_filtrado['Qtd_Vendidos_Normalizada'] = (df_filtrado['Qtd_Vendidos'] - df_filtrado['Qtd_Vendidos'].min()) / \
                                      (df_filtrado['Qtd_Vendidos'].max() - df_filtrado['Qtd_Vendidos'].min())

df_filtrado['Nota_Normalizada'] = (df_filtrado['Nota'] - df_filtrado['Nota'].min()) / \
                                      (df_filtrado['Nota'].max() - df_filtrado['Nota'].min())

plt.figure(figsize=(10, 6));
sns.regplot(data=df_filtrado, x='Nota_Normalizada', y='Qtd_Vendidos_Normalizada', line_kws={'color': 'red'});
plt.title('Gráfico de regressão: Nota x Quantidade vendida (Normalizado)', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Nota do Produto (0-1)', fontsize=12);
plt.ylabel('Quantidade Vendida (0-1)', fontsize=12);
plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("Este gráfico de regressão agora exibe a relação entre a nota e a quantidade vendida em uma escala normalizada. A inclinação da linha de tendência continua a indicar a relação, mas os valores nos eixos são diretamente comparáveis.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Graphic 07 (Density Plot): Price Density Distribution
print("--- Graphic 07: Price Density Distribution ---");

plt.figure(figsize=(10, 6));

sns.kdeplot(df['Preço'], shade=True, color=color_yellow, linewidth=2);

plt.title('Distribuição de densidade de preços', fontsize=16, fontweight='bold', color=color_title);
plt.xlabel('Preço', fontsize=12);
plt.ylabel('Density', fontsize=12);
plt.grid(True, linestyle='--', alpha=0.6);
sns.despine();

plt.show();
print("Este gráfico de densidade fornece uma visualização suave da distribuição de preços de produtos.");
print("-" * 50);
# ////////////////////////////////////////////////////////////////////////////////////////////////
