import joblib
from pubscripts.read_code_ml import read_code

def RF_model_prediction(File,str_type):

    File_source = File
    File_Feature = 'fusion_feature/all_reco_' + str_type + '_remove0.svm'
    File_out = 'result/Bitter_RF_predict_' + str_type + '_result.txt'
    File1 = File_source + '/' + File_Feature
    File2 = File_source + '/' + File_out

    X_test , y_test = read_code(File1,format='%s' % 'svm')
    out=open(File2,'w')
    model = joblib.load('packages/Bitter_RF.model')

    predict = model.predict(X_test)
    predict = list(predict)
    length = len(predict)

    for i in range(length):
        out.write(str(i+1)+':'+str(predict[i])+'\n')
    out.write('\nResult parsing:\n')
    out.write('The format we output is: \nSerial number + bitter peptide prediction result.\n\n')
    out.write('Analysis of bitter peptide prediction results:\n')
    out.write('0: This sequence is predicted by Bitter_RF to be non-bitter peptide. \n')
    out.write('1: This sequence is predicted by Bitter_RF to be bitter peptide. \n')
    out.close()
