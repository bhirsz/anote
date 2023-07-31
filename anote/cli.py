from pathlib import Path
from typing import Optional

import click

from anote.generate import generate_release
from anote.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, prog_name="anote")
def cli():
    pass


@cli.command()
@click.option(
    "-u",
    "--unreleased-dir",
    default="unreleased",
    show_default=True,
    metavar="UNRELEASED DIR",
    help="Directory with unreleased notes",
)
@click.argument(
    "new_version"
)
def generate(new_version: str, unreleased_dir: str):
    unreleased_path = resolve_unreleased_path(unreleased_dir)
    generate_release(new_version, unreleased_path)


def resolve_unreleased_path(unreleased_dir: str) -> Path:
    unreleased_path = Path(unreleased_dir)
    if not unreleased_path.is_dir():
        raise ValueError("TODO")  # TODO
    return unreleased_path
