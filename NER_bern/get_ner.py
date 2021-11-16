import jsonmerge, json, requests, os
from jsonmerge import Merger
from pathlib import Path
from jsonmerge import merge
import numpy as np
import pandas as pd
import os

# send text to bern
def query_raw(text, url="https://bern.korea.ac.kr/plain"):
    return requests.post(url, data={'sample_text': text}).json()

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

def write_parcial_jsons(texts_list):
    for i in range(len(texts_list)):                                  # percorre a lista de textos
        ner = query_raw(texts_list[i])                                  # faz o NER
        Path('./jsons/ner{}.json'.format(i)).touch()
        with open('./jsons/ner{}.json'.format(i), 'w', encoding='utf-8') as f:  
            json.dump(ner, f, indent=4)                                   # escreve o arquivo .json


def merge_all_jsons(directory=r'./jsons/'):
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
    Path('./jsons/ner0.json').touch()
    with open('./jsons/ner0.json', 'r') as f:
        result = json.load(f)
  # adiciona o atributo "parcial_text" nas anotações do 1° arquivo .json (acima)
  # esse atributo será útil para saber de qual bloco de texto a palavras será recuperada depois
    for i in range(len(result['denotations'])):
        result['denotations'][i].update({'parcial_text': 0})
  # percorre o diretório de todos os arquivos .json:
    num_jsons = len(os.listdir(directory))
    for filename in os.listdir(directory):
        if (num_jsons > 0 and num_jsons > 1):
            if (filename != 'final.json' and filename != 'ner0.json' and filename.endswith('.json')):
                Path(directory+filename).touch()
                with open(directory+filename) as f:
                    jsonObject = json.load(f)                                                   # lê o arquivo e cria o objeto json
        else:
            with open('./jsons/ner0.json') as f:
                jsonObject = json.load(f)                                                   # lê o arquivo e cria o objeto json
        
        flag = 'denotations' in jsonObject
        if (flag):
            for i in range(len(jsonObject['denotations'])):                               # percorre as anotações e adiciona o atributo
                if (filename != 'final.json'):
                    jsonObject['denotations'][i].update({'parcial_text': int(filename[3])})
        result = merger.merge(result, jsonObject)                                     # faz o merge das informações
  # escreve o arquivo .json final:
    Path('./jsons/final.json').touch()
    with open('./jsons/final.json', 'w', encoding='utf-8') as f:
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


texto_completo = Path('../tensorboard_inputs/metadata_w2v.tsv').read_text(encoding="utf-8").replace('\n', ' ')
textos_parciais = brake_text(texto_completo)

os.makedirs('./jsons', exist_ok=True) 

write_parcial_jsons(textos_parciais)
merge_all_jsons()

with open('./jsons/final.json', 'r', encoding='utf-8') as f:
    finalJson = json.load(f)