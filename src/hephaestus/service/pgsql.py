from sqlalchemy import create_engine


def get_service(user, pw, host, port, db):
    pgsql_url = 'postgresql://{}:{}@{}:{}/{}'
    pgsql_url = pgsql_url.format(user, pw, host, port, db)
    pgsql_engine = create_engine(pgsql_url, client_encoding='utf8')
    return pgsql_engine
