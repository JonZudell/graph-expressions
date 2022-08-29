import unittest
import repl

class TestRepl(unittest.TestCase):
    def setUp(self):
        repl.CURRENT_SYMBOL = "<ATOM>"
        repl.GRAPH = {}

    def test_identity(self):
        idx = 'identity'
        self.assertEqual(repl.read(idx), idx) 
        self.assertEqual(repl.evaluate(repl.read(idx)), idx) 

    # Test Grammar is a type-2 unambiguous recursive grammar
    # N - Finite Non-Empty Set of Non-Terminal Symbols
    # T – Finite Set of Terminal Symbols
    # Once you have a non-left-recursive, left-factored grammar, recursive descent parsing is (generally) easy to implement.
    def test_no_left_recursion_grammar(self):
        # no production rules implement
        pass

    def test_left_factored_grammar(self):
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
