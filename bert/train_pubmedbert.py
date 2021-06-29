#based on https://github.com/huggingface/blog/blob/master/notebooks/01_how_to_train.ipynb

import torch
from transformers import LineByLineTextDataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling
from transformers import AutoTokenizer
from transformers import AutoModelForMaskedLM, AutoModelForPreTraining 
from pathlib import Path
import os

import torch
print(torch.cuda.is_available())

tokenizer = AutoTokenizer.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext")
model = AutoModelForMaskedLM.from_pretrained('microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext')

model.train()

from transformers import AutoModelForMaskedLM, LineByLineTextDataset

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
    output_dir="./pubmedbert_we4lkd",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_gpu_train_batch_size=32,
    save_steps=10_000,
    save_total_limit=2,
#    prediction_loss_only=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

trainer.save_model("./pubmedbert_we4lkd")
