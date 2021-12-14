# -----------------------------------------------------------------------------
# Created:     04.03.2014
# Copyright:   (c) Josua Schmid 2014
# Licence:     AGPLv3
#
# Sample script for parsing HTML tables
# -----------------------------------------------------------------------------

import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def main():
    url = 'https://w3schools.com/html/html_tables.asp'
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)

    # Get all tables
    pprint(p.tables)

    # Get tables with id attribute
    pprint(p.named_tables)


if __name__ == '__main__':
    main()
