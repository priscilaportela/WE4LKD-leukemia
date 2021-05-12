#based on https://github.com/huggingface/blog/blob/master/notebooks/01_how_to_train.ipynb

import torch
from transformers import DistilBertConfig
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForMaskedLM, DistilBertModel
from transformers import LineByLineTextDataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling

from pathlib import Path

from tokenizers import ByteLevelBPETokenizer

import os

paths = ["../results_file_clean.txt"]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=200, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

os.makedirs('distilbert_we4lkd', exist_ok=True) 
tokenizer.save_model("distilbert_we4lkd")

from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


tokenizer = DistilBertForMaskedLM(
    "./distilbert_we4lkd/vocab.json",
    "./distilbert_we4lkd/merges.txt",
)

tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)

tokenizer.enable_truncation(max_length=512)


import torch
print(torch.cuda.is_available())

from transformers import DistilBertConfig

config = DistilBertConfig(
    vocab_size=52000,
    max_position_embeddings=514,
    type_vocab_size=1,
)

from transformers import DistilBertTokenizerFast

tokenizer = ByteLevelBPETokenizer.from_pretrained("./distilbert_we4lkd", max_len=512)

from transformers import DistilBertForMaskedLM

model = DistilBertForMaskedLM(config=config)

model.num_parameters()

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="../results_file_clean.txt",
    block_size=128,
)

from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./distilbert_we4lkd",
    overwrite_output_dir=True,
    num_train_epochs=4,
    per_gpu_train_batch_size=1,
    save_steps=10000,
    save_total_limit=2,
    prediction_loss_only=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)


trainer.train()

trainer.save_model("./distilbert_we4lkd")


