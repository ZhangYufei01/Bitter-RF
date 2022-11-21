import os

def Feature_Fusion(file,file1,file2,file3):
    os.chdir(file)
    lines=open(file1,'r').readlines()
    lines2=open(file2,'r').readlines()

    type_num=len(lines)

    p=lines[0].split("  ")
    q=lines2[0].split("  ")
    m=len(p)-1
    n=len(q)-1
    out=open('fusion_feature/intermediate file.svm','w')
    for line,line2 in zip(lines,lines2):
        l = line.strip("\n")
        l2 = line2.strip("\n")
        if line[0] == '0':
            l3=l2.lstrip('0')
        else:
            l3=l2.lstrip('1')

        out.write(l+l3+'\n')
        continue
    out.close()

    before=open('fusion_feature/intermediate file.svm','r').readlines()
    out=open(file3,'w')
    x=m
    y=n
    for i in range(type_num):
        a = before[i].split("  ")
        for j in range(0,x+y+1):
            if j<(x+1):
                d=a[j]
            else:
                b=a[j].split(":")
                c=int(b[0])+x
                d=':'.join([str(c),b[1]])
            if(j<x+y):
                out.write(d+'  ')
            else:
                out.write(d)
            continue
    out.close()
    os.remove('fusion_feature/intermediate file.svm')