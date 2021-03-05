from os import path
import unittest

from html_table_parser import HTMLTableParser

class ParserTest(unittest.TestCase):
    def getTestInput(self, input_name: str) -> str:
        with open(path.join(path.dirname(__file__), "test_cases", input_name + ".html")) as f:
            return f.read()
        self.assertTrue(False, "Invalid input file name")

    def test_singleTable(self):
        input = self.getTestInput("single_table")
        print(input)

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        self.assertEqual(3, len(actual[0]))
        self.assertTrue(all([len(a) == 10 for a in actual[0]]))
        current_cell_value = 0
        
        for r in range(3):
            for c in range(10):
                self.assertEqual(current_cell_value, int(actual[0][r][c]))
                current_cell_value = current_cell_value + 1