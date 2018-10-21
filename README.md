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

## CLI

 There is also a command line interface which you can use directly to
generate a CSV:

    html-table-converter -u http://metal-train.de/index.php/fahrplan.html -o metaltrain

If you need help for the supported parameters append `-h`:

    html-table-converter -h

## Credit

Josua Schmid (schmijos) created this and [other contributor](https://github.com/schmijos/html-table-parser-python3/graphs/contributors)

## License

GNU GPL v3
