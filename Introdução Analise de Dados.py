#!/usr/bin/env python
# coding: utf-8

# ### Desafio
# 
# - Empresa Vende Bermudas
# - 5 Lojas
# - Está querendo aumentar as vendas
# - O que fazer?
# - Informações Disponíveis: Base de Vendas

# ### Passo 1 - Trazer sua base de dados para o Python e ver o que tem nela

# In[1]:


import pandas as pd
tabela = pd.read_excel("Vendas.xlsx")
display(tabela)


# ### Passo 2 - Pegar um panorama geral sobre a sua base de dados

# In[2]:


faturamento_total = tabela ["Valor Final"].sum()
print (faturamento_total)


# ### Passo 3 - Começar sua análise Top -> Down

# In[6]:


#faturamento por loja

faturamento_por_loja = tabela [["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)


# ### Passo 4 - Entrar no detalhe pra entender

# In[10]:


faturamento_por_produto = tabela [["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)


# De acordo com nossa base de dados, vimos que o produto "Bermuda Liso" é o mais vendido na loja "Iguatemi Campinas", com isso o aumento das vendas foram efetivas, sabendo então que para aumentarmos o lucro da empresa, precisamos distribuir a "Bermuda Lisa" para todas as outras lojas.
