# Análise Exploratória de Dados de E-commerce

---

### 📖 Visão Geral do Projeto

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (AED)** sobre um conjunto de dados de e-commerce. A análise visa extrair insights valiosos sobre o comportamento de vendas e a relação entre diferentes variáveis, como preço, descontos, avaliações e quantidade vendida. Para isso, são utilizadas diversas visualizações de dados, permitindo uma compreensão clara e detalhada das características do conjunto.

### 📁 Fonte de Dados

O projeto utiliza o arquivo `ecommerce_estatistica.csv`.

### 🛠️ Ferramentas Utilizadas

* **Python:** Linguagem de programação principal para a análise.
* **Pandas:** Biblioteca para manipulação e análise de dados.
* **Matplotlib e Seaborn:** Bibliotecas para a criação de visualizações de dados.

### 📈 Etapas da Análise

1.  **Leitura e Limpeza dos Dados:** O arquivo CSV é lido em um DataFrame do Pandas. Os dados ausentes são tratados e a base é preparada para a análise.
2.  **Análise Detalhada:** São exploradas as estatísticas descritivas (média, mediana, desvio padrão, etc.) e as correlações entre as variáveis para identificar padrões e relações.
3.  **Visualização de Dados:** Uma série de gráficos é criada para representar visualmente os dados e os insights extraídos. Cada gráfico é projetado para destacar uma característica específica, com títulos e rótulos de eixos claros para facilitar a interpretação.

### 📊 Gráficos Gerados

* **Histograma:** Para visualizar a distribuição de variáveis numéricas.
* **Gráfico de Dispersão:** Para analisar a relação e a correlação entre duas variáveis quantitativas.
* **Mapa de Calor:** Para identificar a força da correlação entre múltiplas variáveis.
* **Gráfico de Barras:** Para comparar a frequência de categorias.
* **Gráfico de Pizza:** Para mostrar a proporção de cada categoria em relação ao todo.
* **Gráfico de Densidade:** Para visualizar a suavidade da distribuição de uma variável.
* **Gráfico de Regressão:** Para exibir a linha de melhor ajuste de um modelo de regressão linear.

---

# Dashboard de Análise de E-commerce (EBAC)

Uma análise detalhada dos dados de vendas para descobrir insights valiosos.

---

## Gráfico 1: Distribuição de Notas dos Produtos

![Gráfico de Distribuição de Notas dos Produtos](img/Dist_Notas_Produtos.png)

**NOTAS:** O gráfico mostra que a maioria dos produtos é avaliada com notas altas, indicando a satisfação geral dos clientes com a qualidade dos itens em nossa loja.

---

## Gráfico 2: Top 10 Marcas Mais Vendidas

![Gráfico Top 10 Marcas Mais Vendidas](img/TOP10.png)

**NOTAS:** Este gráfico de barras destaca as 10 marcas com o maior volume de vendas, oferecendo uma visão clara de nossa liderança de mercado e das marcas mais populares.

---

## Gráfico 3: Relação entre Preço, Quantidade Vendida e Nota

![Gráfico de Dispersão de Preço x Quantidade Vendida](img/relations.png)

**NOTAS:** A análise revela que os maiores volumes de vendas se concentram nas faixas de preço entre 50-100 e 125-180, sugerindo que esses são os pontos de preço ideais para o nosso público.

---

## Gráfico 4: Matriz de Correlação

![Mapa de Calor da Matriz de Correlação](img/MatrixCorrelacao.png)

**NOTAS:** Este mapa de calor confirma uma forte correlação positiva entre a quantidade vendida e o número de avaliações, indicando que produtos com mais feedback dos clientes tendem a ter maior sucesso de vendas.

---

## Gráfico 5: Distribuição de Produtos por Gênero

![Gráfico de Pizza da Distribuição por Gênero](img/Dist_Produtos.png)

**NOTAS:** O gráfico de pizza ilustra a distribuição de nossos produtos, destacando a predominância de categorias de produtos para os gêneros Feminino e Masculino em nossa loja.

---

## Gráfico 6: Regressão: Nota x Quantidade Vendida

![Gráfico de Regressão de Nota x Vendas](img/Regressao.png)

**NOTAS:** O gráfico de regressão normalizado mostra a relação entre a nota de um produto e a quantidade vendida. A inclinação positiva na linha de tendência sugere que a qualidade percebida pelo cliente é um fator-chave para o volume de vendas.

---

## Gráfico 7: Distribuição de Densidade dos Preços

![Gráfico de Densidade dos Preços](img/dist_densidade.png)

**NOTAS:** Este gráfico de densidade oferece uma visualização clara dos preços de nossos produtos. A área mais concentrada na curva indica a faixa de preço onde a maioria de nossos produtos está posicionada.
