"""test simple table.

html table taken from
https://www.w3schools.com/html/html_tables.asp
"""
from html_table_parser.parser import HTMLTableParser
table = """
<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
"""

def test_table():
    """test simple table."""
    exp_res = [[
        ['Firstname', 'Lastname', 'Age'],
        ['Jill', 'Smith', '50'],
        ['Eve', 'Jackson', '94']
    ]]
    from html_table_parser import HTMLTableParser
    parser = HTMLTableParser()
    parser.feed(table)
    assert exp_res == parser.tables

