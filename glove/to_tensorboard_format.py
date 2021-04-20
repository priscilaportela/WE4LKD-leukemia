vector_list = [v.strip() for v in open("vectors.txt", encoding="utf-8")]

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

