from sqlalchemy.orm import Session

from .. import settings as C
from ..service import pgsql

pgsql_engine = pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA)
session = Session(pgsql_engine)


def load(*args):
    # for arg in args:
    #     className = arg.__class__.__name__
    #     if className == 'str':
    #         print(arg)
    #     else:
    #         print(className)
    #         if className == 'visit_occurrence':
    #             print(arg.visit_start_datetime)

    # session = Session(pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA))
    # Person = mysql_base.classes.person
    for arg in args:
        className = arg.__class__.__name__
        # classDef = mysql_base.classes[className]
        if className == 'person':
            res = session.merge(arg)
        else:
            yield arg
    session.commit()
