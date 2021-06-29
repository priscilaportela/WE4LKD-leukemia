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

df_metadata = pd.read_csv('https://s3.console.aws.amazon.com/s3/object/we4lkd?region=us-east-1&prefix=metadata_w2v.tsv', 
                          sep='\t', 
                          header=None)
df_vectors = pd.read_csv('https://s3.console.aws.amazon.com/s3/object/we4lkd?region=us-east-1&prefix=vectors_w2v.tsv', sep='\t', header=None)

st.write(df_metadata.head())
st.write(df_vectors.head())

st.markdown('## Paravras mais proximas')
#chosen_word_vector = df.c1[a.c1 == 8].index.tolist()
