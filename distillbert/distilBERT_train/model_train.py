import os

cmd =	"""
  python run_language_modeling.py
    --train_data_file ../../results_file_clean.txt
    --output_dir ./model
    --model_type distilbert
    --mlm
    --block_size 128
    --config_name .
    --tokenizer_name .
    --do_train
    --learning_rate 1e-4
    --num_train_epochs 10
    --save_total_limit 2
    --save_steps 2000
    --per_gpu_train_batch_size 8
    --seed 42
""".replace("\n", " ")

os.system(cmd)
