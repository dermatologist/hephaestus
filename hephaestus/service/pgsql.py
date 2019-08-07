from sqlalchemy import create_engine

"""
Use this if all tables are in the public schema
"""


def get_service(user, pw, host, port, db):
    pgsql_url = 'postgresql://{}:{}@{}:{}/{}'
    pgsql_url = pgsql_url.format(user, pw, host, port, db)
    pgsql_engine = create_engine(pgsql_url, client_encoding='utf8')
    return pgsql_engine


"""
Maintain CDM tables in one schema and vocabulary tables in another

"""


def get_cdm_service(user, pw, host, port, db, schema="cdm"):
    pgsql_url = 'postgresql://{}:{}@{}:{}/{}?currentSchema={}'
    pgsql_url = pgsql_url.format(user, pw, host, port, db, schema)
    pgsql_engine = create_engine(pgsql_url, client_encoding='utf8')
    return pgsql_engine


def get_vocab_service(user, pw, host, port, db, schema="vocabulary"):
    pgsql_url = 'postgresql://{}:{}@{}:{}/{}?currentSchema={}'
    pgsql_url = pgsql_url.format(user, pw, host, port, db, schema)
    pgsql_engine = create_engine(pgsql_url, client_encoding='utf8')
    return pgsql_engine
