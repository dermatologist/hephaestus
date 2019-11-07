from sqlalchemy import create_engine

from .. import settings as C

"""
Reader reads engine from the vocabulary schema for automaping
and vocabulary search

Used by load-> init and transform init

    # https://stackoverflow.com/questions/9298296/sqlalchemy-support-of-postgres-schemas

"""


def get_schema_engine(vocab):
    # https://stackoverflow.com/questions/9298296/sqlalchemy-support-of-postgres-schemas
    dbschema = '{},public'  # Searches left-to-right
    dbschema = dbschema.format(vocab)
    pgsql_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
    pgsql_url = pgsql_url.format(C.CDM_USER_NAME, C.CDM_USER_PASS,
                                 C.CDM_USER_HOST, C.CDM_USER_PORT, C.CDM_USER_DB)
    engine = create_engine(
        pgsql_url,
        connect_args={'options': '-csearch_path={}'.format(dbschema)})
    return engine


# def get_reader():
#     # https://stackoverflow.com/questions/9298296/sqlalchemy-support-of-postgres-schemas
#     dbschema = '{},public'  # Searches left-to-right
#     dbschema = dbschema.format(C.CDM_USER_VOCAB)
#     pgsql_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
#     pgsql_url = pgsql_url.format(C.CDM_USER_NAME, C.CDM_USER_PASS,
#                                  C.CDM_USER_HOST, C.CDM_USER_PORT, C.CDM_USER_DB)
#     engine = create_engine(
#         pgsql_url,
#         connect_args={'options': '-csearch_path={}'.format(dbschema)})
#     return engine


"""
Writes to the CDM schema

Used by load

"""

# def get_writer():
#     # https://stackoverflow.com/questions/9298296/sqlalchemy-support-of-postgres-schemas
#     dbschema = '{},public'  # Searches left-to-right
#     dbschema = dbschema.format(C.CDM_USER_SCHEMA)
#     pgsql_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
#     pgsql_url = pgsql_url.format(C.CDM_USER_NAME, C.CDM_USER_PASS,
#                                  C.CDM_USER_HOST, C.CDM_USER_PORT, C.CDM_USER_DB)
#     engine = create_engine(
#         pgsql_url,
#         connect_args={'options': '-csearch_path={}'.format(dbschema)})
#     return engine
