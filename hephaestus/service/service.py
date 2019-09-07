from sqlalchemy.ext.automap import automap_base

import hephaestus.service.mysql as mysql
import hephaestus.service.pgsql as pgsql
from hephaestus import settings as C


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    try:
        mysql_engine = mysql.get_service(C.SOURCE_USER_NAME, C.SOURCE_USER_PASS, C.SOURCE_USER_HOST, C.SOURCE_USER_PORT, C.SOURCE_USER_DB)
        mysql_base = automap_base()
        mysql_base.prepare(mysql_engine, reflect=True, name_for_scalar_relationship=name_for_scalar_relationship)
    except:
        mysql_engine = ""
        mysql_base = ""

    try:
        pgsql_engine = pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA)
        pgsql_base = automap_base()
        pgsql_base.prepare(pgsql_engine, reflect=True)
    except:
        pgsql_engine = ""
        pgsql_base = ""

    return {
        'mysql_engine': mysql_engine,
        'pgsql_engine': pgsql_engine,
        'mysql_base': mysql_base,
        'pgsql_base': pgsql_base,

    }


def name_for_scalar_relationship(base, local_cls, referred_cls, constraint):
    name = referred_cls.__name__.lower() + "_ref"
    return name
