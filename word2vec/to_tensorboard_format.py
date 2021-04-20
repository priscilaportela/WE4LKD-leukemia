from gensim.models import Word2Vec
import numpy as np

model = Word2Vec.load('model.bin')

metadata = []
word_vectors = []
for idx, key in enumerate(model.wv.vocab):
    metadata.append(key)
    word_vectors.append(model.wv[key].tolist())

with open("metadata.tsv", 'w', encoding='utf-8') as output:
    for m in metadata:
        output.write(str(m) + '\n')

with open("vectors.tsv", 'w', encoding='utf-8') as output:
    for vw in word_vectors:
        vw = map(str, vw)
        output.write('\t'.join(vw) + '\n')



