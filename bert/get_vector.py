import torch
import pandas as pd
from transformers import BertConfig
from transformers import AutoTokenizer, BertTokenizer
from transformers import RobertaForMaskedLM, BertModel
from transformers import LineByLineTextDataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling
from pathlib import Path
from tokenizers import ByteLevelBPETokenizer
import numpy as np

df = pd.read_csv('../tensorboard_inputs/metadata_w2v.tsv', header=None)
word_list = list(df[0])

word_vectors = []
words = []

tokenizer = AutoTokenizer.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext")
model = BertModel.from_pretrained('./pubmedbert_we4lkd/')

for w in word_list:
    try:
        input_ids = torch.tensor(tokenizer.encode(w)).unsqueeze(0)  # Batch size 1
        outputs = model(input_ids)
        last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
        last_layer = last_hidden_states[-1]
        words.append(w)
        word_vectors.append(last_layer[-4:].mean(0).tolist())
        print(w)
    except:
        pass

with open("./vectors_pubmedbert.tsv", 'w', encoding='utf-8') as output:
    for vw in word_vectors:
        vw = map(str, vw)
        output.write('\t'.join(vw) + '\n')

with open("./metadata_pubmedbert.tsv", 'w', encoding='utf-8') as output:
    for m in words:
        output.write(str(m) + '\n')
