# -*- coding: utf-8 -*-
"""setup."""
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="html-table-parser-python3",
    version="0.1.0",
    description="A small and simple HTML table parser not requiring any external module.",
    license="AGPL-3.0",
    author="schmijos",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    entry_points={
        'console_scripts': ['html-table-converter=html_table_parser.html_table_converter::main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ]
)
