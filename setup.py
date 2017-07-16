# -*- coding: utf-8 -*-
"""setup."""
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="html-table-parser-python3",
    version="0.1.1",
    description="A small and simple HTML table parser not requiring any external module.",
    license="AGPLv3",
    author="Josua Schmid",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    entry_points={
        'console_scripts': ['html-table-converter=html_table_parser.html_table_converter:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    zip_safe=False,
    # metadata for upload to PyPI
    # taken from http://setuptools.readthedocs.io/en/latest/setuptools.html
    # see above for author, description and license
    author_email="josua.schmid@renuo.ch",
    keywords="python3 html table parser",
    url="https://github.com/schmijos/html-table-parser-python3",
)
