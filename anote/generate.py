import re
from pathlib import Path
from typing import List, Optional

from jinja2 import Template

# from jinja2.exceptions import TemplateError TODO


class ReleaseFragment:
    def __init__(self, path, order, section, extension):
        self.path = path
        self.order = order
        self.section = section
        self.extension = extension


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


def get_release_fragments(unreleased_path: Path) -> List[ReleaseFragment]:
    """Find files matching release fragment pattern and return list of them.

    Pattern is: order.section_name.extension
    For example: 2.fixes.rst
    """
    fragment_pattern = re.compile("([0-9]+)\.([^.]+)\.([^.]+)")
    fragments = []
    for file in unreleased_path.iterdir():
        if file.is_dir():
            continue
        fragment_match = fragment_pattern.match(file.name)
        if fragment_match is None:
            continue
        order, section, extension = fragment_match.groups()
        fragments.append(ReleaseFragment(file, order, section, extension))
    return fragments


def generate_release(version: str, unreleased_path: Path, template):
    print(f"Generating release notes for {version}")
    template = get_template_from_path(template, unreleased_path)
    fragments = get_release_fragments(unreleased_path)
    # later in template we can refer to fixes, features as list of strings (simple as it is)
    # --clear-notes to remove *.rst
