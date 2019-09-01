import urllib.request
import urllib.request

import pandas as pd
import pkg_resources
from sqlalchemy import MetaData, Table, Integer, Column, String
from sqlalchemy.orm import sessionmaker

from hephaestus.models.cci_model import CciModel
from hephaestus.service import pgsql
from hephaestus import settings as C

Session = sessionmaker(bind=pgsql.get_schema_engine(C.CDM_USER_SCHEMA))

class Cci(object):

    def __init__(self):
        self._cci_code = ''
        self._cci_short = ''
        self._cci_long = ''
        self._session = Session()

    @property
    def cci_code(self):
        return self._cci_code

    @property
    def cci_short(self):
        return self._cci_short

    @property
    def cci_long(self):
        return self._cci_long

    @cci_code.setter
    def cci_code(self, cci_code):
        self._cci_code = cci_code
        _c = self._session.query(CciModel).filter_by(cci_code=cci_code).one()
        self._cci_short = _c.cci_short
        self._cci_long = _c.cci_long


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
