import torch
from transformers import RobertaConfig
from transformers import RobertaTokenizerFast
from transformers import RobertaForMaskedLM, RobertaModel
from transformers import LineByLineTextDataset
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling
from pathlib import Path
from tokenizers import ByteLevelBPETokenizer


def get_word_vector(word):

    tokenizer = RobertaTokenizerFast.from_pretrained('./tentativa')
    model = RobertaModel.from_pretrained('./tentativa')

    input_ids = torch.tensor(tokenizer.encode("leukemia")).unsqueeze(0)  # Batch size 1

    outputs = model(input_ids)
    last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
    last_layer = last_hidden_states[-1]
    return last_layer[-1]
