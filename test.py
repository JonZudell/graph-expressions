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
        with self.subTest():
            io = 'identity'
            self.assertEqual(repl.evaluate(io), io, 'failed to evaluate graph-component "identity"')
        with self.subTest():
            io = 'x'
            self.assertEqual(repl.evaluate(io), io, 'failed to evaluate graph-component "x"')

    def test_match_application(self):
        with self.subTest():
            io = '(x y)'
            is_match, ndx = repl.match_application(io)
            self.assertTrue(is_match)
            self.assertEqual(len(io) - 1, ndx)

        with self.subTest():
            io = '(λx.x y)'
            is_match, ndx = repl.match_application(io)
            self.assertTrue(is_match)
            self.assertEqual(len(io) - 1, ndx)

    def test_evaluate_application(self):
        with self.subTest():
            i = '(λx.x y)'
            expected_o = 'λx.x y'
            o = repl.evaluate(i)
            self.assertEqual(expected_o, o)

    def test_match_abstraction(self):
        pass

    def test_evaluate_abstraction(self):
        with self.subTest():
            io = "λ x . x"
            self.assertEqual(repl.evaluate(io), io, 
                             'failed to evaluate the identity function')

        with self.subTest():
            io = "λ x . y"
            self.assertEqual(repl.evaluate(io), io,
                             'failed to evaluate the constant function (of x) that returns y')

        with self.subTest():
            io = "λ x . λ y . y"
            self.assertEqual(repl.evaluate(io), io,
                             'failed to evaluate the function of x that returns the identity function') 

    def test_no_left_recursion_grammar(self):
        # Left recursion is a case when the left-most non-terminal in a production of a non-terminal is the non-terminal itself (direct left recursion) or through some other non-terminal definitions, rewrites to the non-terminal again (indirect left recursion).
        symbols = []
        for key in repl.GRAMMAR.keys():
            symbols.extend(repl.GRAMMAR[key])
        for key in repl.GRAMMAR.keys():
            self.assertFalse(key in symbols, 'grammar has a left recursion')

    def test_left_factored_grammar(self):
        # Left factoring is removing the common left factor that appears in two productions of the same non-terminal.
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
