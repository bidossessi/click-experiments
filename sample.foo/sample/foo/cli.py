import click


@click.group()
@click.option(
    '-c', '--config-uri',
    help='Config URI path'
)
@click.option(
    '--myoption',
    help='My option help')
@click.argument(
    'myarg',
    type=click.STRING)
@click.pass_context
def cli(ctx, config_uri=None, **kwargs):
    """Testing group commands"""
    if ctx.obj and ctx.obj.get('INIT', False):
        click.echo("Application is already configured")
    else:
        print('foo got config uri:', config_uri)


@click.command()
@click.pass_context
def initdb(ctx):
    click.echo('Initialized the database')


@click.command()
@click.pass_context
def dropdb(ctx):
    click.echo('Dropped the database')


cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()
