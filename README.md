# Word embeddings capture latent knowledge discovery
Inspired by [this application](https://github.com/materialsintelligence/mat2vec)

# Setup
```
#create venv
python3 -m venv venv
#activate venv
source venv/bin/activate
#install requirements
pip3 install --ignore-installed -r requirements.txt
```

# Run crawler
```
mkdir results
python3 crawler.py
```

# Merge files
This will generate `results_file.txt` 
```
cd bert
python3 merge_txt.py 
```

# Word2Vec
Training the model
```
cd word2vec
python3 train.py
```
Loading the model
```
from gensim.models import Word2Vec
model = Word2Vec.load('model.bin')
```
Access vector for one word
```
model['cytarabin']
```

