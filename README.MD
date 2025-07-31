# Análise de Dados – Global Superstore

## 📋 Descrição do Projeto

Este projeto consiste em uma análise exploratória e visualização de dados do dataset **Global Superstore**, que contém informações sobre vendas, lucros, clientes e logística entre os anos de 2011 e 2014. O objetivo é extrair insights para apoiar decisões estratégicas e entender o comportamento das vendas ao longo do tempo.

---

## 🎯 Objetivos

- Explorar dados de vendas e pedidos
- Analisar lucro por região e vendas por categoria
- Estudar comportamento dos clientes por segmento, cidade e estado
- Avaliar modos de envio e sazonalidade dos pedidos
- Preparar dados para criação de dashboards no Power BI

---

## 🛠 Tecnologias e Bibliotecas Utilizadas

- Python 3.x  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
- Power BI (para dashboards e visualização interativa)

---

## 📊 Descrição do Dataset

O dataset contém aproximadamente 51 mil registros de pedidos, com as seguintes principais colunas traduzidas para português:

- ID do Pedido  
- Data do Pedido  
- Data de Envio  
- Modo de Envio  
- Segmento do Cliente  
- Cidade, Estado, País  
- Categoria e Subcategoria do Produto  
- Vendas, Lucro, Desconto  
- Prioridade do Pedido  

---

## 📁 Estrutura do Projeto

```
analise-superstore/
│
├── dados/
│   ├── brutos/
│   │   └── global_superstore.csv
│   └── processados/
│       └── dados_limpos.csv
│
├── notebooks/
│   └── 01_analise_global_superstore.ipynb
│
├── outputs/
│   └── graficos/
│   ├── tabelas/
│
└── README.md
```
---

## 📈 Gráficos

Abaixo os principais gráficos gerados (todos estão salvos na pasta `/outputs/graficos/`):

| Gráfico                   | Descrição                                      |
|---------------------------|------------------------------------------------|
| `desconto_vs_lucro.png`   | Análise da relação entre desconto e lucro      |
| `lucro_por_cidade.png`    | Lucro total por cidade                          |
| `lucro_por_regiao.png`    | Lucro total por região                          |
| `modos_envio.png`         | Distribuição dos modos de envio utilizados     |
| `pedidos_por_ano.png`     | Quantidade de pedidos por ano                   |
| `pedidos_por_mes.png`     | Quantidade de pedidos por mês (agregado)       |
| `segmentos_clientes.png`  | Distribuição dos segmentos de clientes         |
| `top_estados_pedidos.png` | Top 10 estados com mais pedidos                 |
| `vendas_ao_longo_do_tempo.png` | Evolução das vendas ao longo do tempo      |
| `vendas_por_categoria.png`| Vendas totais por categoria                      |
| `vendas_por_estado.png`   | Vendas totais por estado                         |

---

## 📖 Fonte dos Dados

- Dataset: [Global Super Store Dataset - Kaggle](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset/data)

---

## 📌 Principais Insights

- O número de pedidos apresentou **crescimento constante entre 2011 e 2014**, indicando expansão do negócio.  
- Os meses de **Setembro, Novembro e Dezembro** concentram a maior parte dos pedidos, apontando sazonalidade nas vendas.  
- O segmento **Consumer** domina o mercado, seguido pelos segmentos **Corporate** e **Home Office**.  
- O modo de envio mais utilizado é o **Standard Class**, respondendo por quase metade dos pedidos.  
- As cidades com maior volume de pedidos são **New York City, Los Angeles** e **Philadelphia**.  
- Estados como **Califórnia, Inglaterra** e **Nova York** lideram em quantidade de pedidos.  
- A categoria **Technology** lidera em volume de vendas, seguida por **Furniture** e **Office Supplies**.  
- A região **Central** é responsável pelo maior lucro total, seguida pelas regiões **North** e **North Asia**.  
- A análise da relação entre **desconto e lucro** revela padrões importantes para otimizar preços e promoções.  
- A análise temporal mostra tendências e sazonalidades importantes para planejamento estratégico.

---

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/GabrielRodrigues11/analise-superstore.git
```

## 💼 Autor

**Gabriel Rodrigues**  
Analista de TI em transição para a área de dados. Apaixonado por tecnologia e por transformar dados em soluções visuais e práticas.