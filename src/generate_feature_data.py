import json
import csv
import pandas as pd
from operator import itemgetter
def merge_list(list1,list2):
    final_list = list(set(list1) | set(list2))
    return final_list
gene={}
drug={}
disease={}
species={}
pathway={}
mutation={}
data_dict={'gene':gene,'drug':drug,'disease':disease,'species':species,'pathway':pathway,'mutation':mutation}
myfile = open("../dat/proc/name_entity.txt", "r")
for index,line in enumerate(myfile):
    if len(line)==0:
        continue
    data = json.loads(line)
    denotation = data['denotations']
    text = data['text']

    for entity in denotation:
        obj = entity['obj']
        span = entity['span']
        begin = span['begin']
        end = span['end']
        if text[begin:end] in data_dict[obj]:
            data_dict[obj][text[begin:end]].append(index)
        else:
            data_dict[obj][text[begin:end]]=[index]

myfile.close()

index_dict={}
for disease_key in disease.keys():
    if 'liver injury' != disease_key and 'hepatotoxicity' != disease_key and 'hepatic injury' != disease_key and 'nausea and vomiting' != disease_key:
        if len(disease[disease_key]) >=50:
                for index in disease[disease_key]:
                    if not index in index_dict:
                        index_dict[index]=['Disease '+disease_key]
                    else:
                        index_dict[index].append('Disease '+disease_key)

for gene_key in gene.keys():
    if 'CYP 3A4' != gene_key:
        if len(gene[gene_key]) >= 50:
            for index in gene[gene_key]:
                if not index in index_dict:
                    index_dict[index] = ['Gene '+gene_key]
                else:
                    index_dict[index].append('Gene '+gene_key)

for drug_key in drug.keys():
    if len(drug[drug_key]) >= 50:
        for index in drug[drug_key]:
            if not index in index_dict:
                index_dict[index] = ['Drug '+drug_key]
            else:
                index_dict[index].append('Drug '+drug_key)

term_list=[]
for i in range(0,14361):
    if i in index_dict:
        term_list.append(', '.join(index_dict[i]))
    else:
        term_list.append('')
dfObj = pd.DataFrame(term_list)
dfObj.to_csv('../dat/proc/feature.tsv', sep='\t',index=False)