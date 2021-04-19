import json

config = {
	"architectures": [
		"DistilBertForMaskedLM"
	],
    "model_type": "distilbert",
    "vocab_size": 50000,
    "max_position_embeddings": 66	
}

with open("config.json", 'w') as fp:
    json.dump(config, fp)

tokenizer_config = {
	"max_len": 64
}

with open("tokenizer_config.json", 'w') as fp:
    json.dump(tokenizer_config, fp)
