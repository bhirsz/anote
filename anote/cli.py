import click

from anote.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def generate_release(version):
    print(f"Generating release notes for {version}")
    # load # unreleased dir (default, or passed dir)
    # inside unreleased find release.template, or use --template path and load it
    # get all *.rst files and load them
    # pattern is <order_number>.<section>.rst
    # ie 1.fixes.rst, 10.features.rst
    # later in template we can refer to fixes, features as list of strings (simple as it is)
    # --clear-notes to remove *.rst


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, prog_name="anote")
def cli():
    pass


@cli.command()
@click.argument(
    "new_version"
)
def generate(new_version):
    generate_release(new_version)
