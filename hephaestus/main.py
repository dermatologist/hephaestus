import bonobo
import click

from hephaestus import __version__
from hephaestus.service.create_cdm import CreateCdm


@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Will print verbose messages.")
@click.option('--emr', '-m', multiple=False,
              help='ETL')
@click.option('--schema', '-s', multiple=False, default='dad',
              help='Schema for creating CDM')
@click.option('--num', '-n', multiple=False, default=3,
              help='Top N')
@click.option('--cui', '-c', multiple=True, default='',
              help='Cuis as input')
@click.option('--cdm', '-d', multiple=True, default='',
              help='CDM Concepts as input')
@click.option('--fun', '-f', multiple=True, default='',
              help='Functions to execute')
@click.option('--cid', '-i', multiple=True,
              help='A set of contextual ids to work on.')
def cli(verbose, num, cui, cdm, fun, emr, schema, cid):
    if verbose:
        print("verbose")
    if 'similar' in fun:
        if len(cdm) > 0:
            similar_cdm(cdm, num)
    if 'create' in fun:
        if len(schema) > 0:
            create_cdm(schema)
    if 'etl' in fun:
        if len(emr) > 0:
            run_etl(emr)
    if 'anchor' in fun and len(cid) > 0:
        # -schema may be defined, else public
        # read existing concept IDs
        # Usage python main.py -s ohdsi -i 2 -n 20 -f anchor
        create_anchors(schema, cid, num)


def create_anchors(schema, cid, num):
    # process only first cid
    from hephaestus.vocab.cui import Cui
    c = Cui()
    c.read_from_ohdsi(schema, cid[0])
    if num is not None:
        c.find_anchors(num)
    else:
        c.find_anchors()
    c.write_to_ohdsi(schema, cid[0])


def create_cdm(schema):
    c = CreateCdm(schema)
    c.load_cdm()
    c.set_constraints()


def similar_cdm(concepts, num):
    from hephaestus.vocab.cui import Cui
    c = Cui()
    similar_concepts = []
    c.concept_id = concepts
    codes = c.similar_concepts(num)
    for code in codes:
        similar_concepts.append(code[1])
    click.echo(similar_concepts)


def run_etl(emr):
    # parser = bonobo.get_argument_parser()
    # with bonobo.parse_args(parser) as options:
    from hephaestus.service.get_graph import get_graph
    bonobo.run(
        get_graph(emr)
    )


def main_routine():
    click.echo("_________________________________________")
    click.echo("Hephaestus v: " + __version__)
    cli()  # run the main function


if __name__ == '__main__':
    main_routine()
