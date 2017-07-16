html-table-parser-python3
=========================

This module consists of just one small class.
Its purpose is to parse HTML tables without help of external modules.
Everything I use is part of python 3.
Instead of installing this module, you can just copy the class located in *parse.py* into your own code.

Getting Started
---------------

Installing
~~~~~~~~~~

Run pip install to this repo

.. code:: bash

 pip install git+https://github.com/schmijos/html-table-parser-python3.git

How to use
~~~~~~~~~~

Probably best shown by example using [pyenv](https://github.com/pyenv/pyenv)
for convenience:

    pyenv local
    python example_of_usage.py

or input below code in python console:

.. code:: python

 import urllib.request
 from pprint import pprint
 from html_table_parser import HTMLTableParser

 target = 'https://www.twitter.com'

 # get website content
 req = urllib.request.Request(url=target)
 f = urllib.request.urlopen(req)
 xhtml = f.read().decode('utf-8')

 # instantiate the parser and feed it
 p = HTMLTableParser()
 p.feed(xhtml)
 pprint(p.tables)


The parser returns a nested lists of tables containing rows containing cells as strings.
Tags in cells are stripped and the tags text content is joined.
The console output for parsing all tables on the twitter home page looks like this:

.. code:: python

 >>>
  [[['', 'Anmelden']],
  [['Land', 'Code', 'Für Kunden von'],
   ['Vereinigte Staaten', '40404', '(beliebig)'],
   ['Kanada', '21212', '(beliebig)'],
   ...
   ['3424486444', 'Vodafone'],
   ['Zeige SMS-Kurzwahlen für andere Länder']]]

see also example_of_usage.py for the full source code.

CLI
~~~

There is also a command line interface which you can use directly to generate a CSV:


.. code:: bash

 html-table-converter -u http://metal-train.de/index.php/fahrplan.html -o metaltrain

If you need help for the supported parameters append `-h`:

.. code:: bash

 html-table-converter -h


Running the tests
~~~~~~~~~~~~~~~~~

tba

Versioning
~~~~~~~~~~

We use SemVer for versioning. For the versions available, see the tags on this repository.

License
~~~~~~~

This project is licensed under the AGPLv3- see the *LICENSE* file for details

Acknowledgments
~~~~~~~~~~~~~~~

- Hat tip to anyone who's code was used
