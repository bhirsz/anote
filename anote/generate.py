import re
from collections import defaultdict
from pathlib import Path
from typing import List, Optional

from jinja2 import Template

# from jinja2.exceptions import TemplateError TODO


class ReleaseFragment:
    def __init__(self, path, order, section, extension):
        self.path = path
        self.order = int(order) if order is not None else order
        self.section = section
        self.extension = extension

    def load_fragment(self):
        with open(self.path) as fp:
            return fp.read()


class ReleaseNote:
    def __init__(
        self, version: str, fragments: List[ReleaseFragment], template: Template
    ):
        self.version = version
        self.fragments = fragments
        self.template = template

    def get_template_env(self):
        sections = defaultdict(list)
        for fragment in self.fragments:
            sections[fragment.section].append(fragment)
        for section, fragments in sections.items():
            sections[section] = sorted(fragments, key=lambda x: x.order)
        env = {"version": self.version}
        for section, fragments in sections.items():
            if len(fragments) == 1 and fragments[0].order is None:
                env[section] = fragments[0].load_fragment()
            else:
                env[section] = [fragment.load_fragment() for fragment in fragments]
        return env

    def generate(self):
        return self.template.render(**self.get_template_env())


def get_template_from_path(template: Optional[str], template_directory: Path) -> str:
    if template is None:
        template_path = template_directory / "template.jinja"
    else:
        template_path = Path(template)
    if not template_path.is_file():
        raise ValueError(f"Template path does not exist: {template_path}")  # TODO
    with open(template_path) as fp:
        return fp.read()


def load_template(template: str, template_directory: Path = None) -> Template:
    return Template(get_template_from_path(template, template_directory))


def get_release_fragments(unreleased_path: Path) -> List[ReleaseFragment]:
    """Find files matching release fragment pattern and return list of them.

    Pattern is: order.section_name.extension
    For example: 2.fixes.rst
    """
    fragment_pattern = re.compile("(?P<section>[^.]+)\.?(?P<order>[0-9]+)?\.(?P<extension>[^.]+)")
    fragments = []
    for file in unreleased_path.iterdir():
        if file.is_dir():
            continue
        fragment_match = fragment_pattern.match(file.name)
        if fragment_match is None:
            continue
        fragments.append(ReleaseFragment(file, fragment_match.group("order"), fragment_match.group("section"), fragment_match.group("extension")))
    return fragments


def generate_release(version: str, unreleased_path: Path, template):
    print(f"Generating release notes for {version}")
    template = load_template(template, unreleased_path)
    fragments = get_release_fragments(unreleased_path)
    release_notes = ReleaseNote(version, fragments, template)
    with open(f"{version}.rst", "w") as fp:
        fp.write(release_notes.generate())
    # --clear-notes to remove *.rst
