#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import csv

import json
import fileinput

import codecs

with open("in.json", 'rb') as f:
    data = f.read()

#print(str(data)[2:100])
#print(str(data)[-100:-1])
data = str(data)[2:-1]
print(data[-100:])
print(data.count('\n}'))
print(len(data))
#print(len(data))
data = data.replace('\\n}', '\\n}-----')
print(data[-100:])
data = data.split('-----')


long = []
short = []
jsons = []

for p in data[0:-1]:
    try:
        jfk = json.loads(codecs.decode(p, 'unicode_escape'))
        jsons.append(jfk)
        long.append(jfk['graph']['sentence'])
        short.append(jfk['headline'])

    except ValueError:
        print("Houve erro")
        print(ValueError)
        print(p[0:100])


print(len(jsons), len(data))

print("teste")

print(data[0][:100])

# Salva o csv
dataset = {'Long': long, 'Short': short}

df = pd.DataFrame(dataset, columns = ['Long', 'Short'])

df.to_csv (r'out.csv', index = None, header=True, quoting = csv.QUOTE_ALL)
