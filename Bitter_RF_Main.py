from Main_RF_Predict import Main_RF_Predict
from Main_Feature_operation import Main_Feature_operation
from Main_Feature import Main_Feature
from Main_Raw_Data import Main_Raw_Data
from Main_data_name import Main_data_name
from Main_delete import  Main_delete


print('Please put your Amino acid sequence in: data folder')
print('For specific formats, please refer to our example file.')
print('Please enter your unpredicted data path and file name (for example: D:/bioinfor/Bitter-RF/data/example.txt).' )
File_data = input("path: ")
if (File_data != ''):
    print('\n')
    print('Bitter_RF is running:')

    List = Main_data_name(File_data)
    File_source = List[0]
    str_type = List[1]
    Main_Raw_Data(File_source, str_type)
    Main_Feature(File_source, str_type)
    Main_Feature_operation(File_source, str_type)
    Main_RF_Predict(File_source,str_type)
    Main_delete(File_source,str_type)

    print('\n')
    print("Bitter_RF bitter peptide predictions have been stored in : result folder, please consult.")
