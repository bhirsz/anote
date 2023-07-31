from setuptools import setup

from anote.version import __version__


README = ""
CLASSIFIERS = """
Development Status :: 3 - Alpha
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Topic :: Utilities
Intended Audience :: Developers
""".strip().splitlines()
KEYWORDS = "automation releasenotes changelog"
DESCRIPTION = "Release notes generator"
PROJECT_URLS = {
    # "Documentation": "https://robocop.readthedocs.io/en/stable",
    "Issue tracker": "https://github.com/bhirsz/anote/issues",
    "Source code": "https://github.com/bhirsz/anote",
}


setup(
    name="anote",
    version=__version__,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bhirsz/anote",
    # download_url="https://pypi.org/project/anote",
    author="Bartlomiej Hirsz",
    author_email="bartek.hirsz@gmail.com",
    license="Apache License 2.0",
    platforms="any",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=["anote"],
    project_urls=PROJECT_URLS,
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=[
        "click==8.1.*",
        "jinja2>=3.0,<4.0",
    ],
    extras_require={
        "dev": [
            "black",
            "coverage",
            "pytest",
        ]
    },
    entry_points={"console_scripts": ["anote=anote.cli:cli"]},
)
