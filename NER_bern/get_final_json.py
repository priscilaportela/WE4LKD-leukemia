import jsonmerge, json, requests, os
from jsonmerge import Merger
from pathlib import Path
from jsonmerge import merge
import numpy as np
import pandas as pd
import os

def merge_all_jsons(directory=r'./content/jsons/'):
    # define o schema (regras para o merge)
    schema = {
             "properties": {
                 "denotations": {
                     "mergeStrategy": "append"
                 }
             }
         }
    # cria o objeto de merge:
    merger = Merger(schema)
    # armazena as informações do 1° arquivo .json, para depois adicionar mais informações a ele:
    with open('./content/jsons/ner0.json', 'r') as f:
        result = json.load(f)
  # adiciona o atributo "parcial_text" nas anotações do 1° arquivo .json (acima)
  # esse atributo será útil para saber de qual bloco de texto a palavras será recuperada depois
    for i in range(len(result['denotations'])):
        result['denotations'][i].update({'parcial_text': 0})
  # percorre o diretório de todos os arquivos .json:
    for filename in os.listdir(directory):
        if (filename != 'final.json' and filename != 'ner0.json' and filename.endswith('.json')):
            with open(directory+filename) as f:
                jsonObject = json.load(f)                                                   # lê o arquivo e cria o objeto json
        flag = 'denotations' in jsonObject
        if (flag):
            for i in range(len(jsonObject['denotations'])):                               # percorre as anotações e adiciona o atributo
                jsonObject['denotations'][i].update({'parcial_text': int(filename[3])})
        result = merger.merge(result, jsonObject)                                     # faz o merge das informações
  # escreve o arquivo .json final:
    with open('./content/jsons/final.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4)


# função que cria o data frame a partir do .json gerado pela BERN
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

merge_all_jsons()

with open('./content/jsons/final.json', 'r', encoding='utf-8') as f:
    finalJson = json.load(f)

df = create_data_frame(finalJson)

df.to_csv('ner_bern.csv', index=False)
