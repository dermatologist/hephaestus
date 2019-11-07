import bonobo

from src.hephaestus.extract import cci_extract, dad_extract
from src.hephaestus.load import cci_load
from src.hephaestus.transform import dad_transform, cci_transform, dad_transform_2
from ..load import dad_load, dad_load_2


def get_graph(emr):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """

    graph = bonobo.Graph()
    if emr == 'dad':
        graph.add_chain(dad_extract.read_dad,  # should not include ()
                        dad_transform.transform,
                        dad_transform_2.transform2,
                        dad_load.load,
                        dad_load_2.load2,
                        )
    elif emr == 'cci':
        graph.add_chain(cci_extract.read_cci,  # should not include ()
                        cci_transform.transform,
                        cci_load.load,
                        )
    return graph
