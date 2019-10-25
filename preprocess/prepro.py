#preprocessamento

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import csv

import nltk
import numpy as np

import json
import fileinput

import codecs


#load
long = []
short = []

base = pd.read_csv("out.csv")


#steming e remove stop words

stop_words = set(nltk.corpus.stopwords.words('english'))


porter = nltk.stem.porter.PorterStemmer()

features = []

for i in range(len(base.Long)):
    lg = nltk.tokenize.word_tokenize(base.Long[i])
    st = nltk.tokenize.word_tokenize(base.Short[i])
    lgg = ""
    stt = ""
    for j in lg:
        p = porter.stem(j).lower()
        if not j in stop_words:
            if not j in features:
                features.append(p)
            lgg = lgg + " " + p
    for j in st:
        p = porter.stem(j).lower()
        if not j in stop_words:
            if not j in features:
                features.append(p)
            stt = stt + " " + p

    long.append(lgg)
    short.append(stt)


#npl = np.zeros((len(features), len(long)), dtype = int)
#nps = np.zeros((len(features), len(long)), dtype = int)

with open("outmat.csv", "a", encoding="utf-8") as a:
    for i in features:
        a.write(i+',')
    for i in features:
        a.write(','+i)
    a.write('\n')
    
    for i in range(len(long)):
        npl = np.zeros((2*len(features),), dtype = int)
        for j in long[i]:
            try:
                p = features.index(j)
                npl[p] += 1
            except ValueError:
                pass
        for j in short[i]:
            try:
                p = features.index(j)
                npl[p+len(features)-1] += 1
            except ValueError:
                pass
        vs = 0
        for j in npl:
            vs += j
            a.write('' + str(j) + ',')
        print(vs)
        a.write('\n')
        
    
    
#for i in range(len(long)):
    #for j in long[i]:
        #p = features.index[j]
        #npl[i][p] += 1
    #for j in short[i]:
        #p = features.index[j]
        #npl[i][p] += 1


# Salva o csv
dataset = {'Long': long, 'Short': short}

df = pd.DataFrame(dataset, columns = ['Long', 'Short'])

df.to_csv (r'outStem.csv', index = None, header=True, quoting = csv.QUOTE_ALL)
