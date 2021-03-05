from os import path
from typing import List
import unittest

from html_table_parser import HTMLTableParser

class ParserTest(unittest.TestCase):
    def getTestInput(self, input_name: str) -> str:
        with open(path.join(path.dirname(__file__), "test_cases", input_name + ".html")) as f:
            return f.read()
        self.assertTrue(False, "Invalid input file name")

    def checkTableValues(self, actual: List[List[str]], num_rows: int, num_cols: int, expected_values: List[str]):
        self.assertEqual(num_rows, len(actual))
        self.assertTrue(all([len(a) == num_cols for a in actual]))
        current_cell_index = 0

        for r in range(num_rows):
            for c in range(num_cols):
                self.assertEqual(expected_values[current_cell_index], actual[r][c])
                current_cell_index = current_cell_index + 1

    def checkNumericTableValues(self, actual: List[List[str]], num_rows: int, num_cols: int, initial_value: int):
        expected_values = [str(i) for i in range(initial_value, num_rows * num_cols + initial_value)]
        self.checkTableValues(actual, num_rows, num_cols, expected_values)

    def test_singleTable(self):
        input = self.getTestInput("single_table")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        self.checkNumericTableValues(actual[0], 3, 10, 0)

    def test_decodeCharRefs(self):
        input = self.getTestInput("with_char_ref")

        uut = HTMLTableParser(decode_html_entities=True, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        expected_values = [">", "<", "$", "&", "="]
        self.checkTableValues(actual[0], 1, 5, expected_values)

    def test_keepCharRefs(self):
        input = self.getTestInput("with_char_ref")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        expected_values = ["", "", "", "", ""]
        self.checkTableValues(actual[0], 1, 5, expected_values)

    def test_twoTables(self):
        input = self.getTestInput("two_tables")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(2, len(actual))

        self.checkNumericTableValues(actual[0], 3, 10, 0)
        self.checkNumericTableValues(actual[1], 3, 10, 100)