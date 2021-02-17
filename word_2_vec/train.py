from pathlib import Path
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.models.phrases import Phrases, Phraser
import gensim


paths = [str(x) for x in Path("../../results/").glob("**/*.txt")]
sentences = []

for p in paths:
    print(p)
    with open(p, 'r') as f:
        try:
            abstract = [line.strip() for line in f][0].split('.')
            for a in abstract:
                sentences.append(a)
        except:
            pass

sentences = list(set(sentences))

print('all sentences!')

# train model
model = Word2Vec(sentences, min_count=2)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# save model
model.save('model_w2v.bin')
