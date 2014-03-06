#-------------------------------------------------------------------------------
# Name:        html_table_parser
# Purpose:     Simple class for parsing an (x)html string to extract tables.
#              Written in python3
#
# Author:      Josua Schmid
#
# Created:     05.03.2014
# Copyright:   (c) Josua Schmid 2014
# Licence:     GPLv3
#-------------------------------------------------------------------------------
from html.parser import HTMLParser

class HTMLTableParser(HTMLParser):
    """ This class serves as a html table parser. It is able to parse multiple
    tables which you feed in. You can access the result per .tables field.
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.__in_td = False
        self.__in_th = False
        self.__current_table = []
        self.__current_row = []
        self.__current_cell = []
        self.tables = []

    def handle_starttag(self, tag, attrs):
        """ We need to remember the opening point for the content of interest.
        The other tags (<table>, <tr>) are only handled at the closing point.
        """
        if tag == 'td':
            self.__in_td = True
        if tag == 'th':
            self.__in_th = True

    def handle_data(self, data):
        """ This is where we save content to a cell """
        if self.__in_td ^ self.__in_th:
            self.__current_cell.append(data.strip())

    def handle_endtag(self, tag):
        """ Here we exit the tags. If the closing tag is </tr>, we know that we
        can save our currently parsed cells to the current table as a row and
        prepare for a new row. If the closing tag is </table>, we save the
        current table and prepare for a new one.
        """
        if tag == 'td':
            self.__in_td = False
        if tag == 'th':
            self.__in_th = False

        if (tag == 'td') ^ (tag == 'th'):
            final_cell = " ".join(self.__current_cell).strip()
            self.__current_row.append(final_cell)
            self.__current_cell = []
        if tag == 'tr':
            self.__current_table.append(self.__current_row)
            self.__current_row = []
        if tag == 'table':
            self.tables.append(self.__current_table)
            self.__current_table = []