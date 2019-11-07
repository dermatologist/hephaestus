from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

from .. import settings as C

Base = declarative_base()

"""
This is a class used by sqlalchemy to query the table
"""


class CciModel(Base):
    __tablename__ = C.CDM_USER_CCI_TABLE

    cci_id = Column(Integer, primary_key=True)
    cci_code = Column(String)
    cci_short = Column(String)
    cci_long = Column(String)
