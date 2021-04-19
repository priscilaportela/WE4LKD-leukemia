from pathlib import Path

#from tokenizers import ByteLevelBPETokenizer
from tokenizers import BertWordPieceTokenizer

paths = ['../../results_file_clean.txt']

# Initialize a tokenizer
tokenizer = BertWordPieceTokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=50_000, min_frequency=2,special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

tokenizer.save_model('.')

