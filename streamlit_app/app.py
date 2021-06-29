import streamlit as st
import numpy as np
import pandas as pd

st.markdown('# Relatorio - Pubmedbert')

word_option = st.selectbox(
     'Escolha uma palavra:',
     ('azacitidine', 'venetoclax', 'cytarabine', 'daunorubicin', 'decitabine'))

number_option = st.selectbox(
     'Escolha um numero de vizinhos:',
     (5, 10, 20, 50))

df_metadata = pd.read_csv('metadata_w2v.tsv', sep='\t', header=None)
df_vectores = pd.read_csv('vectors_w2v.tsv', sep='\t', header=None)

print(df_metadata.head())

st.markdown('## Paravras mais proximas')
chosen_word_vector = df.c1[a.c1 == 8].index.tolist()