import urllib.request
import urllib.request

import pandas as pd
import pkg_resources


class Cci(object):
    @staticmethod
    def get_cci():
        _respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        url = 'https://secure.cihi.ca/free_products/ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx'
        print('Downloading cci xlsx...')
        urllib.request.urlretrieve(url, _respath + 'ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx')
        df = pd.read_excel(_respath + 'ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx'
                           , sheet_name='2. 2018 CCI Codes', skiprows=5
                           )  # for an earlier version of Excel, you may need to use the file extension of 'xls'
        df.to_csv(_respath + 'cci-2018.csv')
