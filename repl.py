# repl.py
# -----------------------------------------------------------------------------
# graph-expression
#   A context-free, unambiguous, recursive grammar
#   no left recursion, left factored language.
#   Syntactic Structure The lambda calculus
#   every symbol is seperated by whitespace.
#   The starting symbol is an Atom, atoms self apply
#-----------------------------------------------------------------------------
# Backus–Naur Form
#   https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form
#   Any language structure can be defined by a set of symbol substituion rules
#   Symbols come in two varieties Terminal and Non-Terminal. Any symbol only 
#   occurring on the left is non left recursive.
# BNF syntax
#   <symbol> ::= __expression__
#-----------------------------------------------------------------------------
# Grammar
#   The lambda calculus
#     <ATOM>        ::= <EXPRESSION> | variable
#     <EXPRESSION>  ::= "("<ATOM>")" | <ABSTRACTION> | <APPLICATION>>
#     <ABSTRATION>  ::= lambda <ATOM> dot <ATOM>
#     <APPLICATION> ::= <ATOM> | <APPLICATION> (<ATOM>| <ABSTRACTION>)
# Interpreter
#   Non Deterministic Pushdown Automota
#   Read Evaluate Print Loop
import sys
import re
from signal import signal, SIGINT


GRAMMAR = {}
TERMINAL_REGEX = {}

GRAMMAR["<ATOM>"] = ['graph-component', '<EXPRESSION>']
GRAMMAR["<EXPRESSION>"] = ['(<ATOM>)', '<ABSTRACTION>','<APPLICATION>']
GRAMMAR["<ABSTRATION>"] = ['lambda <ATOM> dot <ATOM>']
GRAMMAR["<APPLICATION>"] = ['<ATOM>', '<APPLICATION> (<ATOM> | <ABSTRACTION>)']

TERMINAL_REGEX["graph-component"] = r'^([a-z]*)(-[a-z]+) $'
TERMINAL_REGEX["lambda"] = r'{lambda|λ}'
TERMINAL_REGEX["dot"] = r'{dot|.}'

LAMBDA_SYMBOL='λ'
CURRENT_SYMBOL="<ATOM>"
GRAPH = {}

def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def read(io):
    if not io:
        return input("")
    return io

def matches_keyword(symbol):
    if symbol in ['lambda', 'dot']:
        return True
    return False

def format_expression(func):
    def wrapper(expression):
        func(regex.sub(r'\W+', expression).lower())
    return wrapper

@format_expression
def evaluate(expression):
    if expression.starts('<'):
        # pass update symbol and pop the 'Symbol off the stack;
        pass
    elif expression.starts_with('(')
        # atom apply value to next
        pass
    elif expression.starts_with('l'):
        # anonymous function declaration
        pass
    else:
        # add new symbol to graph
        pass

def read_evaluate(expression):
    return evaluate(read(expression))

def repl(io):
    while True:
        io = read_evaluate()
        print(io)

if __name__ == '__main__':
    # package structure needed
    io = sys.argv[1]
    print("---------- ge repl.py 0.0.0 ----------")
    signal(SIGINT, handler)
    repl(io)
