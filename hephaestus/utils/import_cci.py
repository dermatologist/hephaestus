import urllib.request
import urllib.request

import pandas as pd
import pkg_resources
from sqlalchemy import MetaData, Table, Integer, Column, String

from hephaestus.service import pgsql
from hephaestus.settings import LocalSettings as C


class Cci(object):
    @staticmethod
    def get_cci():
        engine = pgsql.get_schema_engine(C.CDM_USER_SCHEMA)  # Access the DB Engine
        if not engine.dialect.has_table(engine, C.CDM_USER_CCI_TABLE):  # If table don't exist, Create.
            metadata = MetaData(engine)
            # Create a table with the appropriate Columns
            Table(C.CDM_USER_CCI_TABLE, metadata,
                  Column('cci_id', Integer, primary_key=True, nullable=False),
                  Column('cci_code', String, nullable=False),
                  Column('cci_short', String),
                  Column('cci_long', String))
            metadata.create_all()
        _respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        url = 'https://secure.cihi.ca/free_products/ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx'
        print('Downloading cci xlsx...')
        urllib.request.urlretrieve(url, _respath + 'ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx')
        df = pd.read_excel(_respath + 'ICD-10-CA-and-CCI-Trending-Evolution2-en.xlsx'
                           , sheet_name='2. 2018 CCI Codes', skiprows=5
                           )  # for an earlier version of Excel, you may need to use the file extension of 'xls'
        df.to_csv(_respath + C.SOURCE_USER_CCI_FILE)
