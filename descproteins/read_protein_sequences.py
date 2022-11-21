#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import sys
import re

def read_protein_sequences(file):
    if os.path.exists(file) == False:
        print('Error: file %s does not exist.' % file)
        sys.exit(1)
    with open(file) as f:
        records = f.read()
    if re.search('>', records) == None:
        print('Error: the input file %s seems not in FASTA format!' % file)
        sys.exit(1)
    records = records.split('>')[1:]
    fasta_sequences = []
    for fasta in records:
        array = fasta.split('\n')
        header, sequence = array[0], re.sub('[^ACDEFGHIKLMNPQRSTVWY-]', '-', ''.join(array[1:]).upper())
        header_array = header.split('|')
        name = header_array[0]
        label = header_array[1] if len(header_array) >= 1 else '0'
        label_train = header_array[2] if len(header_array) >= 2 else 'training'
        fasta_sequences.append([name, sequence, label, label_train])
    return fasta_sequences