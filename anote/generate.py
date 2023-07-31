from pathlib import Path
from typing import Optional

from jinja2 import Template

# from jinja2.exceptions import TemplateError TODO


def get_template_from_path(template: Optional[str], template_directory: Path) -> str:
    if template is None:
        template_path = template_directory / "template.jinja"
    else:
        template_path = Path(template)
    if not template_path.is_file():
        raise ValueError(f"Template path does not exist: {template_path}")  # TODO
    with open(template_path) as fp:
        return fp.read()


def load_template(template: str, template_directory: Path = None) -> str:
    return Template(get_template_from_path(template, template_directory))


def generate_release(version, unreleased_path, template):
    print(f"Generating release notes for {version}")
    template = get_template_from_path(template, unreleased_path)
    # load # unreleased dir (default, or passed dir)
    # inside unreleased find template.jinja, or use --template path and load it
    # get all *.rst files and load them
    # pattern is <order_number>.<section>.rst
    # ie 1.fixes.rst, 10.features.rst
    # later in template we can refer to fixes, features as list of strings (simple as it is)
    # --clear-notes to remove *.rst
