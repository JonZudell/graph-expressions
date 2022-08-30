import unittest
import repl

class TestRepl(unittest.TestCase):
    def setUp(self):
        repl.CURRENT_SYMBOL = "<EXPRESSION>"
        repl.GRAPH = {}

    # https://opendsa-server.cs.vt.edu/OpenDSA/Books/PL/html/Semantics.html 
    # validate semantics
    def test_identity(self):
        idx = 'identity'
        self.assertEqual(repl.read(idx), idx) 
        self.assertEqual(repl.evaluate(repl.read(idx)), idx) 

    def test_no_left_recursion_grammar(self):
        # Left recursion is a case when the left-most non-terminal in a production of a non-terminal is the non-terminal itself (direct left recursion) or through some other non-terminal definitions, rewrites to the non-terminal again (indirect left recursion).
        symbols = []
        for key in repl.GRAMMAR.keys():
            symbols.extend(repl.GRAMMAR[key])
        for key in repl.GRAMMAR.keys():
            self.assertFalse(key in symbols)

    def test_left_factored_grammar(self):
        # Left factoring is removing the common left factor that appears in two productions of the same non-terminal. It is done to avoid back-tracing by the parser. Suppose the parser has a look-ahead, consider this example:
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
