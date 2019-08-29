import bonobo

from hephaestus.extract import dad_extract
from hephaestus.load import dad_load
from hephaestus.transform import dad_transform


def get_graph(emr):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """

    graph = bonobo.Graph()
    if emr == 'dad':
        graph.add_chain(dad_extract.read_dad,  # should not include ()
                        bonobo.Limit(10),
                        dad_transform.transform,
                        dad_load.load,
                        )
    return graph
