import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")   


st.write("# Sistema de vendas")



st.sidebar.write("## Cadastrar vendas")
data = st.sidebar.date_input("Data da venda")
vendedor = st.sidebar.selectbox("Vendedor", ["João", "Maria", "Pedro"])
produto = st.sidebar.selectbox("Produto", ["Celular", "Monitor", "Mouse", "Teclado", "Notebook", "Cadeira", "Mesa", "Fone de ouvido", "Webcam", "Microfone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar venda")
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)


st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento:,.2f}" )

grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", barmode="group")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.3)
st.plotly_chart(grafico2)