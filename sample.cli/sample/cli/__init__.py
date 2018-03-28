import click
import os
from importlib import import_module


def import_or_fail(app):
    """Return a tuple with the stripped app name and the imported module or False"""
    try:
        mod = import_module('{}.{}'.format(app, 'cli'))
        return app.split('.')[-1], mod
    except ModuleNotFoundError:
        return False


def import_valid_apps():
    dirs = os.listdir(
        os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            os.pardir,
            os.pardir
        ))
    own_module = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    app_names = [app for app in dirs if app.startswith('sample') and app != own_module and 'egg-info' not in app]

    # import all the required modules
    imported = [import_or_fail(app) for app in app_names]
    # keep only the valid items
    valid = [app_tuple for app_tuple in imported if app_tuple]
    return dict(valid)


class MyCLI(click.MultiCommand):
    """Loads the avaiable clis"""

    def __init__(self, *args, **kwargs):
        super(MyCLI, self).__init__(*args, **kwargs)
        self.available_apps = import_valid_apps()

    def list_commands(self, ctx):
        return self.available_apps

    def get_command(self, ctx, name):
        return self.available_apps[name].cli


@click.command(cls=MyCLI)
@click.option(
    '-c', '--config-uri',
    type=click.Path(exists=True),
    help='Config URI path'
)
@click.pass_context
def cli(ctx, config_uri, **kwargs):
    """Root call"""
    if config_uri:
        # do initialization
        # finally
        ctx.obj = {'INIT': True}
    # If we didn't get a config, it probably means we just need to check the options


if __name__ == '__main__':
    cli()
