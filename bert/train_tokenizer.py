from pathlib import Path
from tokenizers import ByteLevelBPETokenizer

#https://huggingface.co/blog/how-to-train

paths = [str(x) for x in Path("../results/").glob("**/*.txt")]
#utf-8 problem
paths = [p.encode('utf-8', 'replace').decode() for p in paths]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

# Save files to disk
tokenizer.save_model(".", "latentbert")
