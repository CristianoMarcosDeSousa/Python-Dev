# Python Dev
# 📊 Sistema de Vendas

Aplicação web desenvolvida em **Python** com **Streamlit** para cadastro, visualização e análise de vendas.

O sistema permite cadastrar vendas por meio de uma interface lateral, armazenar os registros em um arquivo CSV e visualizar os dados em uma tabela e em um dashboard com indicadores e gráficos interativos.

## 🚀 Funcionalidades

* Cadastro de novas vendas;
* Seleção da data da venda;
* Seleção do vendedor;
* Seleção do produto;
* Registro da quantidade vendida;
* Registro do valor da venda;
* Armazenamento dos dados em arquivo `.csv`;
* Visualização das vendas cadastradas;
* Cálculo do faturamento total;
* Dashboard com gráficos interativos.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Streamlit** — desenvolvimento da interface web;
* **Pandas** — manipulação e armazenamento dos dados;
* **Plotly Express** — criação dos gráficos;
* **CSV** — armazenamento dos registros de vendas.

## 📁 Estrutura do projeto

```text
sistema-vendas/
│
├── app.py
├── vendas.csv
└── README.md
```

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Entre na pasta do projeto

```bash
cd sistema-vendas
```

### 3. Instale as dependências

```bash
pip install streamlit pandas plotly
```

## ▶️ Executando o projeto

Para iniciar a aplicação, execute:

```bash
streamlit run app.py
```

Após o comando, o Streamlit disponibilizará a aplicação no navegador.

## 📈 Dashboard

O sistema apresenta:

### Faturamento total

Exibe o valor total das vendas cadastradas.

### Vendas por vendedor e produto

Gráfico de barras que permite visualizar o valor das vendas por vendedor, agrupado por produto.

### Distribuição das vendas por produto

Gráfico de pizza que apresenta a participação de cada produto no valor total das vendas.

## 💾 Armazenamento dos dados

Os registros são armazenados no arquivo:

```text
vendas.csv
```

A cada nova venda cadastrada, o sistema adiciona o registro ao arquivo CSV.

## 📌 Observações

Este projeto utiliza um arquivo CSV para persistência dos dados, sendo adequado para fins de estudo, prototipagem e pequenas aplicações.

Para ambientes de produção ou aplicações com múltiplos usuários, o armazenamento poderia ser posteriormente substituído por um banco de dados, como **SQLite, PostgreSQL ou MySQL**.

## 👩‍💻 Projeto

Projeto desenvolvido para estudo e prática de desenvolvimento de aplicações web utilizando Python, Streamlit, Pandas e Plotly.

