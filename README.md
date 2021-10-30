# html-table-parser-python3.5+

This module consists of just one small class. Its purpose is to parse HTML
tables without help of external modules. Everything I use is part of python 3.
Instead of installing this module, you can just copy the class located in
*parse.py* into your own code.

## How to use

Probably best shown by example using [pyenv](https://github.com/pyenv/pyenv)
for convenience:

    pyenv local
    python ./example_of_usage.py

The parser returns a nested lists of tables containing rows containing cells
as strings. Tags in cells are stripped and the tags text content is joined.
The console output for parsing all tables on the twitter home page looks
like this:

```
>>> 
[[['', 'Anmelden']],
 [['Land', 'Code', 'Für Kunden von'],
  ['Vereinigte Staaten', '40404', '(beliebig)'],
  ['Kanada', '21212', '(beliebig)'],
  ...
  ['3424486444', 'Vodafone'],
  ['Zeige SMS-Kurzwahlen für andere Länder']]]
```

## CLI

There is also a command line interface which you can use directly to
generate a CSV:

    ./html_table_converter -u http://web.archive.org/web/20180524092138/http://metal-train.de/index.php/fahrplan.html -o metaltrain

If you need help for the supported parameters append `-h`:

    ./html_table_converter -h

## Tests

A set of rudimentary tests have been implemented using Python's built-in unittest framework. Tests must be ran on Python 3.X. To run, use the following command:

    python -m unittest
