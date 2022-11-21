#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
from descproteins.ASDC import ASDC
from descproteins.read_protein_sequences import read_protein_sequences
from packages.Get_Feature import Get_Feature

def Main_Feature(File_source,str_type):
    os.chdir(File_source)
    str1 = 'data/all_'
    str2 = '_rename.txt'
    file_name = str1 + str_type +str2
    sequences = read_protein_sequences(file_name)

    feature_ASDC = ASDC(sequences)

    length = len(feature_ASDC)
    length_ASDC = len(feature_ASDC[0])
    file_out = 'feature/all_' + str_type + '_ASDC.svm'
    out = open(file_out,'w')
    for m in range(1,length):
        list = feature_ASDC[m]
        if m!=1:
            out.write('\n')
        out.write(list[1]+'  ')
        for j in range(2,length_ASDC-1):
            out.write(str(j-1)+':'+str(list[j])+'  ')
        out.write(str(length_ASDC-1 - 1) + ':' + str(list[length_ASDC-1]))
    out.close()

    Get_Feature(File_source,str_type)
    print('Descriptor type: ASDC')
