from sqlalchemy.orm import Session

from .. import settings as C
from ..service import pgsql


def load(*args):
    session = Session(pgsql.get_schema_engine(C.CDM_USER_SCHEMA))
    for arg in args:
        session.merge(arg)
    session.commit()
