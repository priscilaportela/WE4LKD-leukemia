import json
from Bio import Entrez
import os
from pathlib import Path
from datetime import datetime

today_date = datetime.today().strftime('%Y-%m-%d')

search_strings = [
    "Myeloid Leukemia Prognosis",
    "Myeloid neoplasm Prognosis",
    "Myeloid Leukemia Diagnosis",
    "Myeloid neoplasm Diagnosis",
    "Myeloid Leukemia Symptoms",
    "Myeloid neoplasm Symptoms",  
    "Myeloid Leukemia causes",
    "Myeloid neoplasm causes",
    "Myeloid Leukemia Etiology",
    "Myeloid neoplasm Etiology",
    "Myeloid Leukemia Molecular markers",
    "Myeloid neoplasm Molecular markers", 
    "Myeloid Leukemia Therapeutic targets",
    "Myeloid neoplasm Therapeutic targets",
    "Myeloid Leukemia drugs",
    "Myeloid neoplasm drugs", 
    "Myeloid Leukemia Chemotherapy",
    "Myeloid neoplasm Chemotherapy", 
    "Myeloid Leukemia treatment",
    "Myeloid neoplasm treatment",
    "Myeloid Leukemia Target therapy",
    "Myeloid neoplasm Target therapy",    
    "Myeloid Leukemia Clinical outcomes",
    "Myeloid neoplasm Clinical outcomes",
    "Myeloid Leukemia Risk stratification",
    "Myeloid neoplasm Risk stratification",    
    "Myeloid Leukemia Risk factors",
    "Myeloid neoplasm Risk factors", 
    "Myeloid Leukemia Relapse",
    "Myeloid neoplasm Relapse", 
    "Myeloid Leukemia Overall survival",
    "Myeloid neoplasm Overall survival",
    "Leukemia free survival",
    "leukemia Disease free survival",
    "leukemia Progression free survival",
    "Leukemia stem cell",
    "leukemia Drug resistance",
    "leukemia Repurposing drugs",    
    "Autologous bone marrow transplant",
    "Leukemia biology",
    "Daunorubicin",
    "Myelodysplastic syndromes",
    "Myeloproliferative neoplasms",
    "Azacitidine", 
    "Venetoclax",
    "Cytarabine",
    "All-trans retinoic acid and/or arsenic trioxide",
    "Repurposing drugs",
    "Decitabine",
    "Allogeneic bone marrow transplant",
    "Myeloproliferative syndromes",
    "Myeloid Leukemia Molecular markers",
    "Myeloid neoplasm Molecular markers"
]



def search(query):
    Entrez.email = 'priscila.portela.c@gmail.com'
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
        Path('./results/{}'.format(s)).mkdir(parents=True, exist_ok=True)    
    
        results = search('"' + s + '"')
        id_list = results['IdList']
        ids.append(id_list)
        papers = fetch_details(id_list)
        print('{} papers for {} fetched'.format(len(id_list), s))
        for i, paper in enumerate(papers['PubmedArticle']):
            try:
                article_title = paper['MedlineCitation']['Article']['ArticleTitle']
                if article_title[-1] == '.':
                    article_title = article_title[:-1]
                article_abstract = paper['MedlineCitation']['Article']['Abstract']['AbstractText'][0]     
                Path('./results/{}/{}.txt'.format(s, article_title)).touch()
                with open('./results/{}/{}.txt'.format(s, article_title), "a") as myfile:
                    myfile.write(article_abstract)
            except:
                pass

            

