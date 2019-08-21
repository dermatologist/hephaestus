import click


@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Will print verbose messages.")
def cli(verbose):
    if verbose:
        print("verbose")
