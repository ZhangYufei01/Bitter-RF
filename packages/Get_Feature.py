import os

def Get_Feature(File_source,str_type):
    os.chdir(File_source)
    Feature_box = ['AAC', 'APAAC', 'QSOrder', 'DPC', 'DDE', 'SOCNumber', 'PAAC', 'GAAC', 'GDPC']
    for i in range(9):
        operate_str = 'python iLearn-protein-basic.py --file data/all_' + str_type +'_rename.txt --method ' + Feature_box[i] + ' --format svm --out feature/all_' + str_type + '_' + Feature_box[i] +'.svm'
        os.system(operate_str)