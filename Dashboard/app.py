# Importa as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.tools import mpl_to_plotly
from dash import Dash, dcc, html  # Importações atualizadas do Dash

# Opcional: Para silenciar a FutureWarning do pandas.replace
# pd.set_option('future.no_silent_downcasting', True)

# --- 1. Carregar os Dados e Definir as Cores ---
try:
    # ATENÇÃO: Verifique o caminho do arquivo CSV. Se 'app.py' estiver
    # na mesma pasta que 'ecommerce_estatistica.csv', use apenas o nome do arquivo.
    # Se estiver em uma subpasta (ex: 'Dashboard') e o CSV estiver na pasta 'Database'
    # que está um nível acima, '..' pode ser necessário, mas 'ecommerce_estatistica.csv'
    # é mais comum para implantação simples.
    df = pd.read_csv('../Database/ecommerce_estatistica.csv')
except FileNotFoundError:
    print(
        "Erro: O arquivo 'ecommerce_estatistica.csv' não foi encontrado. Por favor, certifique-se de que ele está na mesma pasta que o script.")
    exit()

# --- Correção e Limpeza da coluna 'Qtd_Vendidos' ---
# Mapeamento dos valores de texto para números inteiros
map_qtd_vendidos = {
    '+10mil': 10000,
    '+50mil': 50000,
    '+1000': 1000,
    '+100': 100,
    '+50': 50,
    '+5': 5,
    '+25': 25
}
# Usando .loc para evitar o SettingWithCopyWarning e garantindo a inferência de tipo
df.loc[:, 'Qtd_Vendidos'] = df['Qtd_Vendidos'].replace(map_qtd_vendidos)
df.loc[:, 'Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(int)

# Remove linhas com valores ausentes
df.dropna(inplace=True)

# Define a paleta de cores
color_title = '#211A1A'
color_blue = '#33A1F2'
color_yellow = '#FFD60A'
color_text = '#666'

# --- 2. Geração dos Gráficos (Figuras Plotly) ---

# Gráfico 1: Distribuição de Notas dos Produtos
fig1_mpl, ax1 = plt.subplots(figsize=(10, 6))
# Usando density=True para o histograma e KDE para a mesma escala
counts, bins, _ = ax1.hist(df['Nota'], bins=10, density=True, color=color_blue, edgecolor='black', alpha=0.8);
ax1.set_title('Distribuição de Notas dos Produtos', fontsize=16, fontweight='bold', color=color_title);
ax1.set_xlabel('Nota do Produto', fontsize=12);
ax1.set_ylabel('Densidade', fontsize=12);  # Rótulo alterado para densidade
sns.kdeplot(df['Nota'], ax=ax1, color=color_title, lw=2);  # KDE com cor do título
fig1 = mpl_to_plotly(fig1_mpl)
plt.close(fig1_mpl)

# Gráfico 2: Top 10 Marcas Mais Vendidas
top_10_marcas = df['Marca'].value_counts().nlargest(10).sort_values(ascending=True)
cmap2 = plt.cm.get_cmap('YlOrRd')  # Permanece como está, a warning é informativa
cores_barras = cmap2(top_10_marcas.values / top_10_marcas.values.max())
fig2_mpl, ax2 = plt.subplots(figsize=(12, 8))
ax2.barh(top_10_marcas.index, top_10_marcas.values, color=cores_barras)
ax2.set_title('Top 10 Marcas Mais Vendidas', fontsize=16, fontweight='bold', color=color_title)
ax2.set_xlabel('Quantidade Vendida', fontsize=12)
ax2.set_ylabel('Marca', fontsize=12)
fig2 = mpl_to_plotly(fig2_mpl)
plt.close(fig2_mpl)

# Gráfico 3: Relação entre Preço, Quantidade Vendida e Nota
# Filtrando outliers em Qtd_Vendidos e Preço para melhor visualização
df_filtrado3 = df[(df['Qtd_Vendidos'] < 50000) & (df['Preço'] < 1000)].copy()
fig3 = px.scatter(df_filtrado3, x='Preço', y='Qtd_Vendidos', color='Nota',
                  title='Relação entre Preço, Quantidade Vendida e Nota',
                  labels={'Preço': 'Preço do Produto', 'Qtd_Vendidos': 'Quantidade Vendida', 'Nota': 'Nota do Produto'},
                  color_continuous_scale=px.colors.sequential.YlOrRd)

# Gráfico 4: Matriz de Correlação
colunas_numericas = ['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']
correlacao = df[colunas_numericas].corr()
fig4_mpl, ax4 = plt.subplots(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap=plt.cm.get_cmap('YlOrRd'), fmt=".2f", linewidths=.5,
            ax=ax4)  # Permanece como está
ax4.set_title('Matriz de Correlação entre Variáveis Numéricas', fontsize=16, fontweight='bold', color=color_title)
fig4 = mpl_to_plotly(fig4_mpl)
plt.close(fig4_mpl)

# Gráfico 5: Distribuição de Produtos por Gênero
gender_counts = df['Gênero'].value_counts().sort_values(ascending=True)
total_produtos = gender_counts.sum()
percent_limite = 0.014
gender_counts_filtrado = gender_counts[gender_counts / total_produtos > percent_limite]
outros = total_produtos - gender_counts_filtrado.sum()
gender_counts_filtrado['Outros'] = outros
gender_counts_ordenado = gender_counts_filtrado.sort_values(ascending=True)

cmap_pie = plt.cm.get_cmap('YlOrRd')  # Permanece como está
cores_fatias5_rgba = cmap_pie(gender_counts_ordenado.values / gender_counts_ordenado.values.max())
cores_fatias5_rgb = [f'rgba({int(c[0] * 255)},{int(c[1] * 255)},{int(c[2] * 255)},{c[3]})' for c in cores_fatias5_rgba]

fig5 = go.Figure(data=[go.Pie(labels=gender_counts_ordenado.index, values=gender_counts_ordenado.values,
                              marker_colors=cores_fatias5_rgb,  # Usando cores RGB string
                              textinfo='percent+label', hole=.4)])
fig5.update_layout(title_text='Distribuição de Produtos por Gênero',
                   title_font_color=color_title,
                   title_font_size=16)

# Gráfico 6: Regressão Nota x Quantidade Vendida
df_filtrado6 = df[df['Qtd_Vendidos'] < 50000].copy()
df_filtrado6['Qtd_Vendidos_Normalizada'] = (df_filtrado6['Qtd_Vendidos'] - df_filtrado6['Qtd_Vendidos'].min()) / (
        df_filtrado6['Qtd_Vendidos'].max() - df_filtrado6['Qtd_Vendidos'].min())
df_filtrado6['Nota_Normalizada'] = (df_filtrado6['Nota'] - df_filtrado6['Nota'].min()) / (
        df_filtrado6['Nota'].max() - df_filtrado6['Nota'].min())
fig6 = px.scatter(df_filtrado6, x='Nota_Normalizada', y='Qtd_Vendidos_Normalizada',
                  title='Relação entre Nota e Quantidade Vendida',
                  labels={'Nota_Normalizada': 'Nota do Produto (Normalizada)',
                          'Qtd_Vendidos_Normalizada': 'Quantidade Vendida (Normalizada)'},
                  trendline='ols', trendline_color_override='red')

# Gráfico 7: Distribuição de Densidade dos Preços
fig7_mpl, ax7 = plt.subplots(figsize=(10, 6))
sns.kdeplot(df['Preço'], ax=ax7, color=color_yellow, fill=True, linewidth=2);
ax7.set_title('Distribuição de Densidade dos Preços', fontsize=16, fontweight='bold', color=color_title);
ax7.set_xlabel('Preço', fontsize=12);
ax7.set_ylabel('Densidade', fontsize=12);
fig7 = mpl_to_plotly(fig7_mpl)
plt.close(fig7_mpl)

# --- 3. Criação da Aplicação Dash ---
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Análise de E-commerce',
            style={'textAlign': 'center', 'color': color_title, 'fontFamily': 'Poppins'}),

    html.P(children='Uma análise detalhada dos dados de vendas para descobrir insights valiosos.',
           style={'textAlign': 'center', 'color': color_text, 'fontFamily': 'Poppins'}),

    html.Hr(),

    html.H2(children='Gráfico 1: Distribuição de Notas dos Produtos',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='O gráfico mostra que a maioria dos produtos é avaliada com notas altas, indicando a satisfação geral dos clientes com a qualidade dos itens em nossa loja.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-1', figure=fig1),

    html.H2(children='Gráfico 2: Top 10 Marcas Mais Vendidas',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='Este gráfico de barras destaca as 10 marcas com o maior volume de vendas, oferecendo uma visão clara de nossa liderança de mercado e das marcas mais populares.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-2', figure=fig2),

    html.H2(children='Gráfico 3: Relação entre Preço, Quantidade Vendida e Nota',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='A análise revela que os maiores volumes de vendas se concentram nas faixas de preço entre 50-100 e 125-180, sugerindo que esses são os pontos de preço ideais para o nosso público.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-3', figure=fig3),

    html.H2(children='Gráfico 4: Matriz de Correlação',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='Este mapa de calor confirma uma forte correlação positiva entre a quantidade vendida e o número de avaliações, indicando que produtos com mais feedback dos clientes tendem a ter maior sucesso de vendas.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-4', figure=fig4),

    html.H2(children='Gráfico 5: Distribuição de Produtos por Gênero',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='O gráfico de pizza ilustra a distribuição de nossos produtos, destacando a predominância de categorias de produtos para os gêneros Feminino e Masculino em nossa loja.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-5', figure=fig5),

    html.H2(children='Gráfico 6: Regressão: Nota x Quantidade Vendida',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='O gráfico de regressão normalizado mostra a relação entre a nota de um produto e a quantidade vendida. A inclinação positiva na linha de tendência sugere que a qualidade percebida pelo cliente é um fator-chave para o volume de vendas.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-6', figure=fig6),

    html.H2(children='Gráfico 7: Distribuição de Densidade dos Preços',
            style={'color': color_blue, 'borderBottom': f'2px solid {color_blue}', 'paddingBottom': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.P(
        children='Este gráfico de densidade oferece uma visualização clara dos preços de nossos produtos. A área mais concentrada na curva indica a faixa de preço onde a maioria de nossos produtos está posicionada.',
        style={'fontStyle': 'italic', 'color': color_text, 'fontFamily': 'Poppins'}),
    dcc.Graph(id='graph-7', figure=fig7),
])

# --- 4. Executar a Aplicação ---
if __name__ == '__main__':
    app.run(debug=True)  # Alterado de app.run_server para app.run
