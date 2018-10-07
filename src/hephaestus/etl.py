import bonobo
from bonobo.config import use
from sqlalchemy.orm import Session

import src.hephaestus.service.service as service


@use('mysql_engine', 'mysql_base')
def extract(mysql_engine, mysql_base):
    """Placeholder, change, rename, remove... """
    # yield 'hello'
    # yield 'world'
    session = Session(mysql_engine)
    Patient = mysql_base.classes.concept
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



# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=service.get_services(**options)
        )