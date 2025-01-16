import platform

import click
import uvicorn

import settings

AppConfig = settings.AppConfig


@click.group()
def cli():

    if platform.system() != 'Windows':
        import uvloop  # noqa: WPS433
        uvloop.install()


@cli.command(short_help='start web')
def start():
    """Start REST API application."""
    uvicorn.run(
        'web.create_app:app',
        host=AppConfig.HOST,
        port=AppConfig.PORT,
        reload=True,
    )


if __name__ == '__main__':
    cli()
