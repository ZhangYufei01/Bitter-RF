# Data
The bitter peptide and non_bitter peptide datas are stored in ./data/all_training.txt(512 sequences) and ./data/all_independent.txt(128 sequences).

# Working environment
The work was built in Pycharm Community Edition 2021.1.3.
encoding : utf-8  
environment : Python 3.7
The pandas, matplotlib, joblib, numpy, scikit-learn packages are used for model training.
The packages requirement is stored in : requirements.txt


# How to use
Bitter_RF_Main.py is the tool to predict bitter peptides. 

Environment configuration: pip install -r requirements.txt

Users need to confirm the peptide sequences are correctly placed in ./data folder, and input the correct data address in our program.

Peptide data reference format : ./data/examples.txt
Data address reference format : D:/bioinfor/Bitter-RF/data/examples.txt (Suppose Bitter-RF is installed on D:/bioinfor)

# View results
Finally, you can view the prediction results of Bitter-RF in the : ./result folder