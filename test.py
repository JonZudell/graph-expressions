import unittest
import repl

class TestRepl(unittest.TestCase):
    def setUp(self):
        repl.GRAPH = {}

    def test_read(self):
        io = "identity"
        self.assertEqual(repl.evaluate(repl.read(io)), io) 

    # https://opendsa-server.cs.vt.edu/OpenDSA/Books/PL/html/Semantics.html 
    # validate semantics
    def test_evaluate_identity(self):
        io_pairs = [('identity', 'identity', 'failed to evaluate graph-component "identity"'),
                    ('x', 'x', 'failed to evauate graph-component "x"')]
        for ndx, (i, expected_o, error) in enumerate(io_pairs):
            with self.subTest(i=ndx):
                self.assertEqual(repl.evaluate(i), expected_o, error)

    def test_match_application(self):
        io_pairs = ['(x y)', '(λx.x y)']
        for x, i in enumerate(io_pairs):
            with self.subTest(i=x):
                is_match, ndx = repl.match_application(i)
                self.assertTrue(is_match)
                self.assertEqual(len(i) - 1, ndx)

    def test_evaluate_application(self):
        io_pairs = [('(λ x . x y)',  'λ x . x y'),
                    ('λ x . (x y)', 'λ x . x y')]

        for ndx, (i, expected_o) in enumerate(io_pairs):
            with self.subTest(i=ndx):
                o = repl.evaluate(i)
                self.assertEqual(expected_o, o)

    def test_match_abstraction(self):
        pass

    def test_evaluate_abstraction(self):
        io_pairs = [("λ x . x", 'failed to evaluate the identity function'),
                    ("λ x . y", 'failed to evaluate the identity function'),
                    ("λ x . λ y . y", 'failed to evaluate the function of x that returns the identity function')]

        for ndx, (i, error) in enumerate(io_pairs):
            with self.subTest(i=ndx):
                self.assertEqual(repl.evaluate(i), i, error)

    def test_no_left_recursion_grammar(self):
        # Left recursion is a case when the left-most non-terminal in a 
        # production of a non-terminal is the non-terminal itself
        symbols = []
        for key in repl.GRAMMAR.keys():
            symbols.extend(repl.GRAMMAR[key])
        for key in repl.GRAMMAR.keys():
            self.assertFalse(key in symbols, 'grammar has a left recursion')

    def test_left_factored_grammar(self):
        # Left factoring is removing the common left factor that appears
        # in two productions of the same non-terminal.
        for key in repl.GRAMMAR.keys():
            left_factors = []
            for production in repl.GRAMMAR[key]:
                left_factors.append(production.split(' ')[0])
            self.assertFalse(key in left_factors, 'grammar is not left factored')

    # Eliminate noise
    def test_format_expression(self):
        pass

    # Test our ability to encode data
    def test_church_encoding(self):
        pass

if __name__ == '__main__':
    unittest.main()
