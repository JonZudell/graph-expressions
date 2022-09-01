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
    def test_identity(self):
        io = 'identity'
        self.assertEqual(repl.evaluate(io), io) 

        io = 'x'
        self.assertEqual(repl.evaluate(io), io) 

    def test_application(self):
        io = '(x y)'
        is_match, ndx = repl.match_application(io)
        self.assertTrue(is_match)
        self.assertEqual(len(io) - 1, ndx)

        io = '(λx.x y)'
        is_match, ndx = repl.match_application(io)
        self.assertTrue(is_match)
        self.assertEqual(len(io) - 1, ndx)

    def test_abstraction(self):
        io = "λ x . x"
        self.assertEqual(repl.evaluate(io), io) 

        io = "λ y . y"
        self.assertEqual(repl.evaluate(io), io) 

        io = "λ x . y"
        self.assertEqual(repl.evaluate(io), io) 

        io = "λ x . λ y . y"
        self.assertEqual(repl.evaluate(io), io) 

    def test_no_left_recursion_grammar(self):
        # Left recursion is a case when the left-most non-terminal in a production of a non-terminal is the non-terminal itself (direct left recursion) or through some other non-terminal definitions, rewrites to the non-terminal again (indirect left recursion).
        symbols = []
        for key in repl.GRAMMAR.keys():
            symbols.extend(repl.GRAMMAR[key])
        for key in repl.GRAMMAR.keys():
            self.assertFalse(key in symbols)

    def test_left_factored_grammar(self):
        # Left factoring is removing the common left factor that appears in two productions of the same non-terminal.
        for key in repl.GRAMMAR.keys():
            left_factors = []
            for production in repl.GRAMMAR[key]:
                left_factors.append(production.split(' ')[0])
            self.assertFalse(key in left_factors)

    # Eliminate noise
    def test_format_expression(self):
        pass

    # Test our ability to encode data
    def test_church_encoding(self):
        pass

if __name__ == '__main__':
    unittest.main()
