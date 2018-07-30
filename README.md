# html-table-parser-python3

This module consists of just one small class. Its purpose is to parse HTML
tables without help of external modules. Everything used is part of python 3.

## Installation

    pip install html-table-parser-python3

## How to use

Example Usage:

    import urllib.request
    from pprint import pprint
    from html_table_parser import HTMLTableParser
    
    
    def url_get_contents(url):
        """ Opens a website and read its binary contents (HTTP Response Body) """
        req = urllib.request.Request(url=url)
        f = urllib.request.urlopen(req)
        return f.read()
    
    
    def main():
        url = 'http://www.twitter.com'
        xhtml = url_get_contents(url).decode('utf-8')
    
        p = HTMLTableParser()
        p.feed(xhtml)
        pprint(p.tables)
    
    
    if __name__ == '__main__':
        main()

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

## Credit

All Credit goes to Josua Schmid (schmijos). This is all his work, I just uploaded it to PyPi. Original repository can be found at:

https://github.com/schmijos/html-table-parser-python3


## License

GNU GPL v3
