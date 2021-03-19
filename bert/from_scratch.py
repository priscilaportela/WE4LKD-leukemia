#based on https://github.com/huggingface/blog/blob/master/notebooks/01_how_to_train.ipynb

import torch
from transformers import RobertaConfig
from transformers import RobertaTokenizerFast
from transformers import RobertaForMaskedLM, RobertaModel
from transformers import LineByLineTextDataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling

#configs
config = RobertaConfig(
    vocab_size=52000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)

tokenizer = RobertaTokenizerFast.from_pretrained("./latentbert", max_len=512)
model = RobertaForMaskedLM(config=config)

print('num params: {}'.format(model.num_parameters()))

#training dataset
dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="../results_file.txt", 
    block_size=128,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

print('before trainer')

#trainer
training_args = TrainingArguments(
    output_dir="./latentbert",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_gpu_train_batch_size=64,
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
trainer.save_model("./latentbert")

