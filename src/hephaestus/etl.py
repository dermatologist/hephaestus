import bonobo
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.hephaestus.constants import OMOP_CONSTANTS as C
from bonobo.config import use


@use('engine')
def extract(engine):
    """Placeholder, change, rename, remove... """
    # yield 'hello'
    # yield 'world'
    base = automap_base()
    base.prepare(engine, reflect=True, name_for_scalar_relationship=name_for_scalar_relationship)
    session = Session(engine)
    Patient = base.classes.concept
    # patients = Patient.query.all()
    patients = session.query(Patient).all()
    for patient in patients:
        yield patient

def transform(*args):
    """Placeholder, change, rename, remove... """
    for arg in args:
        yield arg


# @use('session')
def load(*args):
    """Placeholder, change, rename, remove... """
    print(*args)
    # for arg in args:
    #     print(arg)
    #     session.add(arg)
    # session.commit()


def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)

    return graph


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    mysql_url = 'mysql://{}:{}@{}:{}/{}'
    mysql_url = mysql_url.format(C.USER_NAME, C.USER_PASS, C.USER_HOST, C.USER_PORT, C.USER_DB)
    mysql_engine = create_engine(mysql_url, isolation_level="READ UNCOMMITTED")
    # base = automap_base()
    # base.prepare(mysql_engine, reflect=True, name_for_scalar_relationship=name_for_scalar_relationship)
    # session = Session(mysql_engine)

    # users = User.query.all()

    # url = 'postgresql://{}:{}@{}:{}/{}'
    # url = url.format(C.USER_NAME, C.USER_PASS, C.USER_HOST, C.USER_PORT, C.USER_DB)
    # engine = create_engine(url, client_encoding='utf8')
    # base = automap_base()
    # base.prepare(engine, reflect=True)
    # session = Session(engine)
    return {
        'engine': mysql_engine,
        #'base': base,
    }

def name_for_scalar_relationship(base, local_cls, referred_cls, constraint):
    name = referred_cls.__name__.lower() + "_ref"
    return name

# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )