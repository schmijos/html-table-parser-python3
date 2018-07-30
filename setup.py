"""setup."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='html-table-parser-python3',
                 version='0.1.5',
                 description='A small and simple HTML table parser not requiring any external dependency.',
                 url="https://github.com/schmijos/html-table-parser-python3",
                 author="Josua Schmid",
                 author_email="josua.schmid@renuo.ch",
                 maintainer='Arran Hobson Sayers',
                 maintainer_email='ahobsonsayers@gmail.com',
                 license='AGPLv3',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 extras_require={'dev': ['twine>=1.11.0', ], },
                 entry_points={
                     'console_scripts': ['html-table-converter=html_table_parser.html_table_converter:main'],
                 },
                 classifiers=(
                     "Programming Language :: Python :: 3 :: Only",
                     "License :: OSI Approved :: GNU Affero General Public License v3",
                     "Operating System :: OS Independent",
                     "Topic :: Text Processing :: Markup :: HTML")
                 )
                 keywords="python3 html table parser",
)
