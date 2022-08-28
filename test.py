import unittest
import repl

class TestRepl(unittest.TestCase):
    def setUp(self):
        repl.CURRENT_SYMBOL = "<ATOM>"
        repl.GRAPH = {}

    # Test Grammar is a type-2 unambiguous recursive grammar
    def test_no_left_recursion_grammar(self):
        pass

    # Eliminate noise
    def test_format_expression(self):
        pass

    # Test our ability to encode data
    def test_church_encoding(self):
        pass

    # Correctness of REPL
    def test_all_syntax_resolves_to_series_of_terminal_symbols(self):
        pass

if __name__ == '__main__':
    unittest.main()
