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
st.title('Gráficos e opções de filtragem por G4')

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

# Visualizando os dados
st.markdown('---')
st.title('Tabelas de Dataframe')
st.markdown('### Base de dados: Skoob ')
st.dataframe(df)
st.markdown('---')



# Visualização Gráfica
st.title('Visualização Gráfica')
# Valores ausentes
fig = px.bar(x = [0,4,759,759,0,0,2,1,0,0,0,0,0,0,0,0,657,589,0,0],
            y = ['titulo','autor','isbn_13','isbn_10','ano','paginas','idioma', 'editora',
            'rating', 'avaliacao', 'resenha', 'abandonos', 'relendo', 'querem_ler', 'lendo', 
            'leram', 'descricao', 'genero', 'male', 'female'],
            orientation='h', title=" Valores faltantes ",
             labels={'x':'Quantidade','y':'Dados'})
st.plotly_chart(fig, use_container_width=False, sharing='streamlit')






















#Referencias e adicionando sidebar
st.sidebar.markdown('Feito por : grupo G4')
st.sidebar.markdown("- [Github](https://github.com/Taciana3090/Bbooks")