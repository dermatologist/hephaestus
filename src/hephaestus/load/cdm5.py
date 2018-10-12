from bonobo.config import use
from sqlalchemy.orm import Session


@use('mysql_engine', 'mysql_base')
def load(mysql_engine, mysql_base, *args):
    session = Session(mysql_engine)
    Person = mysql_base.classes.person
    print(*args)
