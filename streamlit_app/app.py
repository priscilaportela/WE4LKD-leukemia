import streamlit as st
import numpy as np
import pandas as pd
from scipy import spatial
from itertools import repeat

st.markdown('# Relatorio - WE4LKD')

word_option = st.selectbox(
     'Escolha uma palavra:',
     ('azacitidine', 'venetoclax', 'cytarabine', 'daunorubicin', 'decitabine'))

number_option = st.selectbox(
     'Escolha um numero de vizinhos:',
     (5, 10, 20, 50))

df_metadata = pd.read_csv('s3://we4lkd/metadata_w2v.tsv', 
                          sep='\t', 
                          header=None)
df_vectors = pd.read_csv('s3://we4lkd/vectors_w2v.tsv', sep='\t', header=None)

st.markdown('## {} Paravras mais proximas'.format(number_option))
st.write('Palavra escolhida: {}'.format(word_option))
word_target_index = list(df_metadata[0]).index(word_option)
vector_target = list(df_vectors[0])[word_target_index]

vectors = list(df_vectors[0])
words = list(df_metadata[0])
del vectors[word_target_index]
del words[word_target_index]

#search_closest words
tree = spatial.KDTree(vectors)

closest_words = []
for i in repeat(None, int(number_option)):
    closest_word_index = tree.query(vector_target)[0]
    closest_words.append(words[closest_word_index])
    del vectors[closest_word_index]
    del words[closest_word_index]
    i+=1

st.write(closest_words)


