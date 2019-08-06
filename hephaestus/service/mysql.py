from sqlalchemy import create_engine


def get_service(user, pw, host, port, db):
    mysql_url = 'mysql://{}:{}@{}:{}/{}'
    mysql_url = mysql_url.format(user, pw, host, port, db)
    mysql_engine = create_engine(mysql_url, isolation_level="READ UNCOMMITTED")
    return mysql_engine
