import bonobo
import click

from hephaestus import __version__
from hephaestus.extract import dad_extract
from hephaestus.load import dad_load
from hephaestus.transform import dad_transform
from hephaestus.vocab.cui import Cui


@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Will print verbose messages.")
@click.option('--hephaestus', '-p', multiple=False, default='dad',
              help='ETL')
@click.option('--num', '-n', multiple=False, default=3,
              help='Top N')
@click.option('--cui', '-c', multiple=True, default='',
              help='Cuis as input')
@click.option('--cdm', '-d', multiple=True, default='',
              help='CDM Concepts as input')
@click.option('--fun', '-f', multiple=True, default='',
              help='Functions to execute')
def cli(verbose, num, cui, cdm, fun, hephaestus):
    if verbose:
        print("verbose")
    if 'similar' in fun:
        if len(cdm) > 0:
            similar_cdm(cdm, num)
    if hephaestus == 'dad':
        print("Running ETL")
        run_etl()


def similar_cdm(concepts, num):
    c = Cui()
    similar_concepts = []
    c.concept_id = concepts
    codes = c.similar_concepts(num)
    for code in codes:
        similar_concepts.append(code[1])
    click.echo(similar_concepts)


def get_graph():
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(dad_extract.read_dad,  # should not include ()
                    bonobo.Limit(10),
                    dad_transform.transform,
                    dad_load.load,
                    )
    return graph


def run_etl():
    # parser = bonobo.get_argument_parser()
    # with bonobo.parse_args(parser) as options:
    bonobo.run(
        get_graph()
    )


def main_routine():
    click.echo("_________________________________________")
    click.echo("Hephaestus v: " + __version__)
    cli()  # run the main function


if __name__ == '__main__':
    main_routine()
