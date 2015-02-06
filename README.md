html-table-parser-python3
=========================

This module consists of just one small class. Its purpose is to parse HTML tables without help of external modules. Everything I use is part of python 3. Instead of installing this module, you can just copy the class located in *parse.py* into your own code.

```python
import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser # import the parser class somehow

target = 'http://www.twitter.com'

# get website content
req = urllib.request.Request(url=target)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables)
```

`p.tables` returns nested lists of tables containing rows containig cells as string. Tags in cells are stripped and the tags text content is joined. The console output for parsing all tables on the twitter home page looks like this:

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
