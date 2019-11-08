import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import datetime
import os 
import pkg_resources

"""
Converts dad file with a list of diagnoses and intrerventions in the form of a binary vector:

"""
class DadVector(object):

    def __init__(self):
        self._dad_file = ''
    
    @property
    def dad_file(self):
        return self._dad_file


    @dad_file.setter
    def dad_file(self, dad_file):
        self._dad_file = dad_file


    """
    Number of characters of the ICD 10 and CCI codes to include: Example with the default value of 3, the headers will be as below
    S79,S80,S81,S82,S83,S84,S85,S86,S87,S88,S89,S90,S91,S92,S93,S94,S95,S96,S97,S98,S99,T00,T01,T02,T03
    If 0, the entire value will be used.

    los_bin: If set to true TLOS_CAT_BIN field will be created with 1 = more than 10 days of admission and 0 for less.
    treatment: If true, CCI code vectors will be added.

    """
    def vectorize(self, flag = 3, los_bin=True, treatment = True ):
        _respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'

        df = pd.read_csv(_respath + self._dad_file, header = 0)

        if(flag>0):
            df['D_I10_1'] = df['D_I10_1'].str[:flag]
            df['D_I10_2'] = df['D_I10_2'].str[:flag]
            df['D_I10_3'] = df['D_I10_3'].str[:flag]
            df['D_I10_4'] = df['D_I10_4'].str[:flag]
            df['D_I10_5'] = df['D_I10_5'].str[:flag]

            df['I_CCI_1'] = df['I_CCI_1'].str[:flag]
            df['I_CCI_2'] = df['I_CCI_2'].str[:flag]
            df['I_CCI_3'] = df['I_CCI_3'].str[:flag]
            df['I_CCI_4'] = df['I_CCI_4'].str[:flag]
            df['I_CCI_5'] = df['I_CCI_5'].str[:flag]
            df['I_CCI_6'] = df['I_CCI_6'].str[:flag]
            df['I_CCI_7'] = df['I_CCI_7'].str[:flag]
            df['I_CCI_8'] = df['I_CCI_8'].str[:flag]
            df['I_CCI_9'] = df['I_CCI_9'].str[:flag]
            df['I_CCI_10'] = df['I_CCI_10'].str[:flag]

        morbidity = df[['D_I10_1', 'D_I10_2', 'D_I10_3', 'D_I10_4', 'D_I10_5']]
        interventions = df[['I_CCI_1', 'I_CCI_2','I_CCI_3','I_CCI_4','I_CCI_5', 'I_CCI_6', 'I_CCI_7','I_CCI_8','I_CCI_9','I_CCI_10']]
        demographics = df[['SUB_PROV', 'AGRP_F_D', 'GENDER', 'X_FR_I_T', 'ADM_CAT', 'ENT_CODE', 'X_TO_I_T', 'DIS_DISP', 'WGHT_GRP']]
        los = df[['TLOS_CAT', 'ACT_LCAT', 'ALC_LCAT']]


        if(los_bin):
            los['TLOS_CAT_BIN'] = np.where(los['TLOS_CAT'] >=10, 1, 0)

        # Converts the values to a list
        morbidity['diseases']= morbidity.values.tolist()
        interventions['treatments']=interventions.values.tolist()

        mlb = MultiLabelBinarizer()
        disease_vector = mlb.fit_transform(morbidity['diseases'].dropna())

        # Column names of the dataframe are the class names of multilabel binarizer
        disease_df = pd.DataFrame(data = disease_vector, columns=mlb.classes_)
        treatment_vector = mlb.fit_transform(interventions['treatments'].dropna())
        treatment_df = pd.DataFrame(data = treatment_vector, columns=mlb.classes_)
        if(treatment):
            horizontal_stack = pd.concat([demographics, disease_df, treatment_df, los], axis=1)
        else:
            horizontal_stack = pd.concat([demographics, disease_df, los], axis=1)

        # Remove the empty string and ZZZ
        if(flag>0):
            z = 'Z' * flag
            empty = ' ' * flag
        else:
            z = 'ZZZZZZ'
            empty = "      "

        horizontal_stack = horizontal_stack.drop(columns=z)
        horizontal_stack = horizontal_stack.drop(columns=empty)

        # Save the file
        file_name = _respath + "dad-vector-"+datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+".csv"
        horizontal_stack.to_csv(file_name)

        