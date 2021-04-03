import json
from Bio import Entrez
import os
from pathlib import Path
from datetime import datetime

search_strings = []
with open ('search_strings.txt', 'rt') as file:    
    for line in file:                   
        search_strings.append(line.rstrip('\n'))




def search(query):
    Entrez.email = 'your@email.com' #change here
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='999999',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'priscila.portela.c@gmail.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

contents = []
ids = []

if __name__ == '__main__':
    for s in search_strings:
        print('searching for {}'.format(s))
    
        results = search('"' + s + '"')
        id_list = results['IdList']
        ids.append(id_list)
        papers = fetch_details(id_list)
        s = s.lower().replace(' ', '_')
        Path('./results/{}'.format(s)).mkdir(parents=True, exist_ok=True)
        print('{} papers for {} fetched'.format(len(id_list), s))
        for i, paper in enumerate(papers['PubmedArticle']):
            try:
                article_title = paper['MedlineCitation']['Article']['ArticleTitle']
                if article_title[-1] == '.':
                    article_title = article_title[:-1]
                    article_title = article_title.lower().replace(' ', '_')
                article_abstract = paper['MedlineCitation']['Article']['Abstract']['AbstractText'][0]     
                Path('./results/{}/{}.txt'.format(s, article_title)).touch()
                with open('./results/{}/{}.txt'.format(s, article_title), "a") as myfile:
                    myfile.write(article_abstract)
            except:
                pass

            

