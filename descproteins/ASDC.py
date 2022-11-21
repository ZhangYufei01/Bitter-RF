#!/usr/bin/env python
#_*_coding:utf-8_*_

import re

def ASDC(fastas, **kw):
    AA = kw.get('order', None) if kw.get('order', None) is not None else 'ACDEFGHIKLMNPQRSTVWY'
    encodings = []
    diPeptides = [aa1 + aa2 for aa1 in AA for aa2 in AA]
    header = ['#', 'label'] + diPeptides
    encodings.append(header)

    AADict = {}
    for i in range(len(AA)):
        AADict[AA[i]] = i

    for i in fastas:
        name, sequence, label = i[0], re.sub('-', '', i[1]), i[2]
        code = [name, label]
        tmpCode = [0] * 400
        for j in range(len(sequence) - 2 + 1):
            for t in range(j + 1, len(sequence) - 2 + 2):
                tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[t]]] = tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[t]]] +1
        if sum(tmpCode) != 0:
            tmpCode = [i/sum(tmpCode) for i in tmpCode]
        code = code + tmpCode
        encodings.append(code)

    return encodings