import click


@click.command()
@click.option(
    '-c', '--config-uri',
    help='Config URI path'
)
@click.option(
    '--amount',
    help='Number of greetings.')
@click.argument(
    'name',
    type=click.STRING)
@click.pass_context
def cli(ctx, amount, name, config_uri=None, **kwargs):
    """Simple program that greets NAME for a total of COUNT times."""
    if ctx.obj and ctx.obj.get('INIT', False):
        print('bar says already configured')
    else:
        print('bar got config uri:', config_uri)
    if not amount:
        amount = 1
    for x in range(amount):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    cli()
