from gensim.models import Word2Vec

# define training data
summaries = [s.strip() for s in open('../results_file_clean.txt', encoding='utf-8')]

word_list = []
for s in summaries:
    s = s.split(' ')
    word_list.append(s)    

# train model
model = Word2Vec(word_list, min_count=2)

# save model
model.save('model.bin')
