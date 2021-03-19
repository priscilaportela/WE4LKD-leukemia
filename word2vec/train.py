from gensim.models import Word2Vec

# define training data
summaries = [s.strip() for s in open('../results_file.txt')]

word_list = []
remove_chars = [',', '!', '.', ';', '(', ')',']','[']
for s in summaries:
    s = s.split(' ')
    s = [w.lower().translate({ord(x): '' for x in remove_chars}) for w in s]
    word_list.append(s)    

# train model
model = Word2Vec(word_list, min_count=2)

# summarize the loaded model
#print(model)

# summarize vocabulary
#words = list(model.wv.vocab)
#print(words)

# access vector for one word
#print(model['leukemia'])

# save model
model.save('model.bin')

# load model
#new_model = Word2Vec.load('model.bin')
