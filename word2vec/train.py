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

# save model
model.save('model.bin')
