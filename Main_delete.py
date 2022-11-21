import os

def Main_delete(File_source,str_type):
    os.chdir(File_source)
    File_1 = 'data/all_' + str_type + '_rename.txt'
    os.remove(File_1)
    Feature_box = ['AAC', 'APAAC', 'ASDC','QSOrder', 'DPC', 'DDE', 'SOCNumber', 'PAAC', 'GAAC', 'GDPC']
    for i in range(10):
        File_2 = 'feature/all_' + str_type + '_' + Feature_box[i] + '.svm'
        os.remove(File_2)
    File_3 = 'fusion_feature/all_reco_' + str_type + '_ACC_APAAC_QSOrder_ASDC_DPC_DDE_SOCNumber_PAAC_GAAC_GDPC.svm'
    os.remove(File_3)
    File_4 = 'fusion_feature/all_reco_' + str_type +'_remove0.svm'
    os.remove(File_4)



