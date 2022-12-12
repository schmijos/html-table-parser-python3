from os import path
import unittest

from html_table_parser import HTMLTableParser

class ParserTest(unittest.TestCase):
    def getTestInput(self, input_name: str) -> str:
        with open(path.join(path.dirname(__file__), "test_cases", input_name + ".html")) as f:
            return f.read()
        self.assertTrue(False, "Invalid test_input file name")

    def checkTableValues(self, actual: list[list[str]], num_rows: int, num_cols: int, expected_values: list[str]):
        self.assertEqual(num_rows, len(actual))
        self.assertTrue(all([len(a) == num_cols for a in actual]))
        current_cell_index = 0

        for r in range(num_rows):
            for c in range(num_cols):
                self.assertEqual(expected_values[current_cell_index], actual[r][c])
                current_cell_index = current_cell_index + 1

    def checkNumericTableValues(self, actual: list[list[str]], num_rows: int, num_cols: int, initial_value: int):
        expected_values = [str(i) for i in range(initial_value, num_rows * num_cols + initial_value)]
        self.checkTableValues(actual, num_rows, num_cols, expected_values)

    def test_singleTable(self):
        test_input = self.getTestInput("single_table")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        self.checkNumericTableValues(actual[0], 3, 10, 0)

    def test_withInternalTags(self):
        test_input = self.getTestInput("tags_inside_cells")

        uut = HTMLTableParser(decode_html_entities=False, data_separator='-')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        expected_values = ["0-zero", "1-one", "2-two", "3-three", "4-four", "5-five", "6-six", "7-seven", "8-eight", "9-nine-nuevo"]
        self.checkTableValues(actual[0], 1, 10, expected_values)

    def test_decodeCharRefs(self):
        test_input = self.getTestInput("with_char_ref")

        uut = HTMLTableParser(decode_html_entities=True, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        expected_values = [">", "<", "$", "&", "="]
        self.checkTableValues(actual[0], 1, 5, expected_values)

    def test_keepCharRefs(self):
        test_input = self.getTestInput("with_char_ref")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(1, len(actual))
        expected_values = ["", "", "", "", ""]
        self.checkTableValues(actual[0], 1, 5, expected_values)

    def test_twoTables(self):
        test_input = self.getTestInput("two_tables")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(2, len(actual))

        self.checkNumericTableValues(actual[0], 3, 10, 0)
        self.checkNumericTableValues(actual[1], 3, 10, 100)

    def test_namedTables(self):
        test_input = self.getTestInput("named_tables")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables
        actual_named = uut.named_tables

        self.assertEqual(2, len(actual))
        self.assertEqual(2, len(actual_named))

        self.checkNumericTableValues(actual[0], 3, 10, 0)
        self.checkNumericTableValues(actual[1], 3, 10, 100)

        self.checkNumericTableValues(actual_named["named_table_one"], 3, 10, 0)
        self.checkNumericTableValues(actual_named["named_table_two"], 3, 10, 100)

    def test_nestedTable(self):
        test_input = self.getTestInput("nested_table")

        uut = HTMLTableParser(decode_html_entities=False, data_separator=' ')
        uut.feed(test_input)
        actual = uut.tables

        self.assertEqual(2, len(actual))

        nested_table = actual[0]
        self.checkNumericTableValues(nested_table, 2, 3, 0)

        outer_table = actual[1]
        expected_first_row = ['', '1', '2']
        expected_second_row = ['10', '11', '12']
        self.assertEqual(2, len(outer_table))
        self.assertlistEqual(outer_table[0], expected_first_row)
        self.assertlistEqual(outer_table[1], expected_second_row)
