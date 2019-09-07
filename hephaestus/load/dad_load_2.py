from sqlalchemy.orm import Session

from hephaestus.service import pgsql
from hephaestus import settings as C

pgsql_engine = pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA)
session = Session(pgsql_engine)


def load2(*args):
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
        # className = arg.__class__.__name__
        # classDef = mysql_base.classes[className]
        res = session.merge(arg)
    session.commit()
