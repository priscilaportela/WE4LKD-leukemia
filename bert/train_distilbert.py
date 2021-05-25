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
import torch
print(torch.cuda.is_available())
from transformers import DistilBertConfig


config = DistilBertConfig()

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

from transformers import AutoModelForMaskedLM, DistilBertForMaskedLM

model = AutoModelForMaskedLM.from_pretrained('distilbert-base-uncased')
model.train()

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
    num_train_epochs=1,
    per_gpu_train_batch_size=64,
    save_steps=10_000,
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
