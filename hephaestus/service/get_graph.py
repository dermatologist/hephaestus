import bonobo

from hephaestus.extract import dad_extract, cci_extract
from hephaestus.load import dad_load, cci_load
from hephaestus.transform import dad_transform, cci_transform


def get_graph(emr):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """

    graph = bonobo.Graph()
    if emr == 'dad':
        graph.add_chain(dad_extract.read_dad,  # should not include ()
                        dad_transform.transform,
                        dad_load.load,
                        )
    elif emr == 'cci':
        graph.add_chain(cci_extract.read_cci,  # should not include ()
                        cci_transform.transform,
                        cci_load.load,
                        )
    return graph
