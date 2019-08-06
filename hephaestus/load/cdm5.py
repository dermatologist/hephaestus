from bonobo.config import use
from sqlalchemy.orm import Session


@use('pgsql_engine')
def load(pgsql_engine, *args):
    session = Session(pgsql_engine)
    # Person = mysql_base.classes.person
    for arg in args:
        # className = arg.__class__.__name__
        # classDef = mysql_base.classes[className]
        arg = session.merge(arg)
    session.commit()
