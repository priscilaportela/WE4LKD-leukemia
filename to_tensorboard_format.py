from gensim.models import Word2Vec
import numpy as np
import sys
import os

#create folder if not exists
os.makedirs('tensorboard_inputs', exist_ok=True) 

#parser
embedding = sys.argv[1]

if embedding == 'word2vec':
    model = Word2Vec.load('./word2vec/model.bin')

    metadata = []
    word_vectors = []
    for idx, key in enumerate(model.wv.vocab): 
        metadata.append(key)
        word_vectors.append(model.wv[key].tolist())

    with open("metadata_w2v.tsv", 'w', encoding='utf-8') as output:
    for m in metadata:
        output.write(str(m) + '\n')

    with open("vectors_w2v.tsv", 'w', encoding='utf-8') as output:
        for vw in word_vectors:
            vw = map(str, vw)
            output.write('\t'.join(vw) + '\n')

if embedding == 'glove'
    vector_list = [v.strip() for v in open("./glove/vectors.txt", encoding="utf-8")]

    metadata = []
    word_vectors = []
    for v in vector_list:
        metadata.append(v.split(' ')[0])
        word_vectors.append(v.split(' ')[1:])

    with open("metadata_glove.tsv", 'w') as output:
        for m in metadata:
        output.write(str(m) + '\n')

    with open("vectors_glove.tsv", 'w') as output:
        for vw in word_vectors:
            vw = map(str, vw)
            output.write('\t'.join(vw) + '\n')

