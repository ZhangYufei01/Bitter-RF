
import os
from packages.Feature_Fusion import Feature_Fusion
from packages.Feature_select import Feature_select

def Main_Feature_operation(File_source,str_type):

    Feature_box = ['AAC','APAAC','QSOrder','ASDC','DPC','DDE','SOCNumber','PAAC','GAAC','GDPC']
    path = 'feature/'
    str1 = 'all_'+ str_type
    str2 = '.svm'
    path2 = 'fusion_feature/'
    str1_1 = 'all_reco_'+ str_type
    x = ''
    c = '_ACC'
    for i in range(9):
        x = x + '_' + Feature_box[i]
        if i ==0 :
            a = path + str1 + x +str2
        else :
            a = d
        b = path + str1 + '_' + Feature_box[i+1] +str2
        c = c + '_' + Feature_box[i+1]
        d = path2 + str1_1 + c +str2
        Feature_Fusion(File_source,a,b,d)

    total_name = d

    for i in range(0,8):
        t = 9-i
        r = '_'+Feature_box[t]
        c = c.replace(r,'')
        e = path2 + str1_1 + c + str2
        os.remove(e)


    File2 = str1_1+'_remove0.svm'
    Feature_select(File_source,total_name,File2)

