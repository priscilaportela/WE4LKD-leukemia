import streamlit as st
import numpy as np
import pandas as pd
from scipy import spatial

st.markdown('# Relatorio - WE4LKD')

number_option = st.selectbox(
     'Escolha um numero de vizinhos:',
     (5, 10, 20, 50))

df_metadata = pd.read_csv('s3://we4lkd/metadata_w2v.tsv',
                          sep='\t',
                          header=None)
df_vectors = pd.read_csv('s3://we4lkd/vectors_w2v.tsv', sep='\t', header=None)

st.markdown('## {} Paravras mais proximas'.format(number_option))

for w in ['haematopoietic', 'azacitidine', 'venetoclax', 'cytarabine', 'daunorubicin', 'decitabine']:

    st.write('Palavra escolhida: {}'.format(w))
    word_target_index = list(df_metadata[0]).index(w)
    vector_target = df_vectors.values.tolist()[word_target_index]

    vectors = df_vectors.values.tolist()
    words = list(df_metadata[0])
    del vectors[word_target_index]
    del words[word_target_index]

    #search_closest words
    tree = spatial.KDTree(vectors)

    closest_words = []

    from itertools import repeat
    for i in repeat(None, int(number_option)):
        closest_word_index = tree.query(vector_target)[1]
        closest_words.append(words[closest_word_index])
        del vectors[closest_word_index]
        del words[closest_word_index]

    st.write(closest_words)

st.markdown('## Busca livre - com filtro')
word_search = st.text_input("Palavra a ser buscada")
n_similar = st.text_input("Numero de palavras semelhantes")

word_option = st.selectbox(
     'Escolha um filtro:',
     ('', 'gene', 'disease', 'drug', 'species', 'miRNA', 'mutation'))

