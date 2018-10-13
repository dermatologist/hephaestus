from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = MetaData(bind=con, reflect=True)

    return con, meta


def start():
    Base = automap_base()

    # engine, suppose it has two tables 'user' and 'address' set up
    engine, meta = connect('beapen', '', 'beapen_db', 'localhost', 5432)

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # mapped classes are now created with names by default
    # matching that of the table name.
    # Domain = Base.classes.domain
    # print(Base.classes.keys())
    #
    # for table in meta.tables:
    #     print(table)
    # session = Session(engine)
    #
    # # rudimentary relationships are produced
    # session.commit()
    return Base


if __name__ == "__main__":
    start()
