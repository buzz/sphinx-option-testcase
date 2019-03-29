import click


@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Print verbose messages.")
def cli(verbose):
    pass


if __name__ == '__main__':
    cli()
