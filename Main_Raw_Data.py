import os

def Main_Raw_Data(File_source,str_type):
    os.chdir(File_source)
    File_Raw = File_source +'/data/' + str_type + '.txt'
    lines = open(File_Raw, 'r').readlines()
    File_Raw_rename = File_source +'/data/all_' + str_type + '_rename.txt'
    out = open(File_Raw_rename, 'w')

    seq_num = len(lines)

    for i in range(seq_num):
        fasta1 = '>Seq_'+ str(i+1) +'|0|predicting'
        out.write(fasta1+'\n')
        out.write(lines[i])
    out.close()

