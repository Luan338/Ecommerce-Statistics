import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.tools import mpl_to_plotly
from dash import Dash, dcc, html

# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# Definição das cores para o layout
color_title = '#211A1A' # Preto para títulos
color_primary = '#FF8C00' # Laranja para destaque
color_secondary = '#FFD60A' # Amarelo para ênfase
color_text = '#666' # Cinza para textos
color_blue = '#33A1F2'
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////
# A Dash procura por arquivos estáticos em uma pasta chamada "assets"
# Certifique-se de que suas imagens (.png) estão localizadas nessa pasta,
# com os nomes de arquivo correspondentes abaixo.
# ////////////////////////////////////////////////////////////////////////////////////////////////

# Criação da Aplicação Dash e Layout
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Análise de E-commerce (EBAC)',
            style={'textAlign': 'center', 'color': color_title, 'fontFamily': 'Poppins'}),

    html.P(children='Uma análise detalhada dos dados de vendas para descobrir insights valiosos.',
           style={'textAlign': 'center', 'color': color_text, 'fontFamily': 'Poppins'}),
    html.Hr(),

    html.H2(children='Gráfico 1: Distribuição de Notas dos Produtos',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/Dist_Notas_Produtos.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: O gráfico mostra que a maioria dos produtos é avaliada com notas altas, indicando a satisfação geral dos clientes com a qualidade dos itens em nossa loja.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 2: Top 10 Marcas Mais Vendidas',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/TOP10.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: Este gráfico destaca as marcas que impulsionam a maior parte das vendas, indicando quais delas são as mais populares e confiáveis para os clientes.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 3: Relação entre Preço, Quantidade Vendida e Nota',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/relations.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: As áreas de densidade mais escuras mostram que a maioria dos produtos com notas mais altas e preços mais baixos tendem a ser mais vendidos.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 4: Matriz de Correlação',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/MatrixCorrelacao.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: O mapa de calor revela as relações entre as variáveis. Uma correlação positiva alta entre `Nota` e `Qtd_Vendidos` significa que produtos com notas melhores tendem a vender mais.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 5: Distribuição de Produtos por Gênero',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/Dist_Produtos.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: A distribuição por gênero mostra a concentração de produtos em categorias específicas, o que pode ser útil para direcionar o marketing.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 6: Regressão: Nota x Quantidade Vendida (Normalizado)',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/Regressao.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: A linha de regressão exibe a relação entre a nota e a quantidade vendida em uma escala normalizada. A inclinação da linha de tendência indica a relação entre as variáveis.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),

    html.H2(children='Gráfico 7: Distribuição de Densidade dos Preços',
            style={'color': color_primary, 'borderTop': f'2px solid {color_primary}', 'paddingTop': '10px',
                   'marginTop': '2em', 'fontFamily': 'Poppins'}),
    html.Img(src='assets/dist_densidade.png', style={'width': '100%', 'height': 'auto'}),
    html.P(
        children='NOTAS: Este gráfico de densidade fornece uma visualização suave da distribuição de preços de produtos, destacando as faixas de preço mais comuns.',
        style={'color': color_text, 'fontFamily': 'Poppins'}),
])

# ////////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    app.run(debug=True)