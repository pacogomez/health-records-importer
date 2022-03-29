__copyright__ = 'Copyright (C) 2021 Paco Gomez'
__license__ = 'GNU GPLv3'

import click
import yaml


@click.group()
@click.option('-f', '--filename', type=click.Path(exists=True))
@click.option('-c', '--config', type=click.Path(exists=True))
@click.option('-q', '--quiet', is_flag=True, default=False)
@click.pass_context
def cli(ctx, filename, config, quiet):
    ctx.ensure_object(dict)
    ctx.obj['filename'] = filename
    if config is not None:
        with open(config) as file:
            ctx.obj['config'] = yaml.load(file, Loader=yaml.FullLoader)
    ctx.obj['quiet'] = quiet


@click.command('version')
@click.pass_context
def version_cmd(ctx):
    cfg = ctx.obj['config']
    print(cfg)


cli.add_command(version_cmd)

if __name__ == 'health_records_importer.hri':
    cli(obj={}, auto_envvar_prefix='HRI')
