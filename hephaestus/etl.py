import bonobo

import hephaestus.extract.test as test
import hephaestus.load.test as testload
import hephaestus.service.service as service
import hephaestus.transform.openmrs_cdm5 as testtransform


def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(test.extract, testtransform.transform, testload.load)

    return graph


if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=service.get_services(**options)
        )
