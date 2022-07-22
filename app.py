# importando as bibliotecas
import streamlit as st
import os 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
from PIL import Image


# Adicionando um titulo
st.title('Gráficos e opções de filtragem')

# importando conjunto de dados
df = pd.read_csv('https://github.com/Taciana3090/Bbooks/raw/master/data/dados.csv', delimiter=',') # --> caminho para o arquivo com os dados  


# Padronização dos nomes
orig_cols = list(df.columns) 
new_cols = [] 
for col in orig_cols:     
    new_cols.append(col.strip().replace('  ', ' ').replace(' ', '_').lower())
df.columns = new_cols

# Utilizando Markdown
st.markdown('---')
st.markdown('# Sobre a Base de Dados')
st.markdown('''Análise de dados exploratórios diferentes, agrupamento de livros por tópicos/categorias, 
mecanismo de recomendação baseado em conteúdo usando campos diferentes da descrição do livro.''')
st.markdown('---')
