from os import path
from typing import List
import unittest

from html_table_parser import HTMLTableParser

class ParserTest(unittest.TestCase):
    def getTestInput(self, input_name: str) -> str:
        with open(path.join(path.dirname(__file__), "test_cases", input_name + ".html")) as f:
            return f.read()
        self.assertTrue(False, "Invalid input file name")

    def checkTableValues(self, actual: List[List[str]], initial_value: int):
        self.assertEqual(3, len(actual))
        self.assertTrue(all([len(a) == 10 for a in actual]))
        current_cell_value = initial_value

        for r in range(3):
            for c in range(10):
                self.assertEqual(current_cell_value, int(actual[r][c]))
                current_cell_value = current_cell_value + 1

    def test_singleTable(self):
        input = self.getTestInput("single_table")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        self.checkTableValues(actual[0], 0)

    def test_twoTables(self):
        input = self.getTestInput("two_tables")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(2, len(actual))

        self.checkTableValues(actual[0], 0)
        self.checkTableValues(actual[1], 100)