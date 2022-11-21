#对indep去除全0


def Feature_select(file,file1,file2):
    file_1=file+'/fusion_feature/zero_one_test.txt'
    file1_1=file+'/'+file1
    file2_1=file+'/fusion_feature/'+file2
    lines=open(file_1,'r').readlines()
    lines2=open(file1_1,'r').readlines()
    out=open(file2_1,'w')


    p = lines[0].split("  ")
    len_seq = len(lines2)

    for m in range(len_seq):
        a=lines2[m].split('  ')
        for j in range(0,1337):
            if(int(p[j])!=0):
                out.write(a[j]+'  ')
            else:
                continue
        out.write(a[1337])
    out.close()


