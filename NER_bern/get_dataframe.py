import jsonmerge, json, requests, os
from jsonmerge import Merger
from pathlib import Path
from jsonmerge import merge
import numpy as np
import pandas as pd

def brake_text(text, n=1024):
  words = iter(text.split(' '))
  lines, current = [], next(words)
  for word in words:
      if len(current) + 1 + len(word) > n:
          lines.append(current)
          current = word
      else:
          current += " " + word
  lines.append(current)
  return lines

def create_data_frame(jsonObject):
  tokens = []
  entities = []

  # percorre as anotações do arquivo .json final:
  for i in jsonObject['denotations']:
    start = i['span']['begin']
    end = i['span']['end']
    tokens.append(textos_parciais[i['parcial_text']][start:end])      # extrai a palavra
    entities.append(i['obj'])                                         # extrai o token
  
  return pd.DataFrame(dict(zip(tokens, entities)).items(), columns=['token', 'entity'])   # retorna o data frame

texto_completo = Path('../tensorboard_inputs/metadata_w2v.tsv').read_text(encoding='utf-8').replace('\n', ' ')
textos_parciais = brake_text(texto_completo)

with open('./content/jsons/final.json', 'r', encoding='utf-8') as f:
      finalJson = json.load(f)

df = create_data_frame(finalJson)

df.to_csv('ner_final.csv', index=False)
