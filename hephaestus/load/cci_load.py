from sqlalchemy.orm import Session

from hephaestus.service import pgsql
from hephaestus import settings as C


def load(*args):
    session = Session(pgsql.get_schema_engine(C.CDM_USER_SCHEMA))
    for arg in args:
        session.merge(arg)
    session.commit()
