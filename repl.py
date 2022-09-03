# repl.py
# -----------------------------------------------------------------------------
# Interpreter
#   Read Evaluate Print Loop
import sys
import re
from signal import signal, SIGINT
from collections import OrderedDict

GRAPH = OrderedDict()
GRAMMAR = OrderedDict()
TERMINAL_LEXEMES = OrderedDict()
NON_TERMINAL_LEXEMES = OrderedDict()

GRAMMAR["<EXPRESSION>"] = ['graph-component',
                           '( <EXPRESSION> )',
                           'λ <EXPRESSION> . <EXPRESSION>']

# Terminal Lexeme
TERMINAL_LEXEMES["graph-component"] = re.compile(r'[a-z](-[a-z])?')

# Non-Terminal Lexeme
NON_TERMINAL_LEXEMES["( <EXPRESSION> )"] = 'application'
NON_TERMINAL_LEXEMES["λ <EXPRESSION> . <EXPRESSION>"] = 'abstraction'

LAMBDA_SYMBOL='λ'

# Helpers
def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def match_abstraction(io):
    pass

def match_application(io):
    parentheses_count = 0
    for ndx, character in enumerate(io):
        if character == '(':
            parentheses_count = parentheses_count + 1
        elif character == ')':
            parentheses_count = parentheses_count - 1
            if parentheses_count == 0:
                return (True, ndx)
            elif parenthese_count == -1:
                raise Exception("Unmatched Parentheses encountered at ndx")
    return (False, 0)

def clean_io(io):
    return io.strip().replace('\s+', ' ')

def evaluate(io):
    for key in TERMINAL_LEXEMES.keys():
        if TERMINAL_LEXEMES[key].match(io):
            if key == 'graph-component':
                return io
    for key in NON_TERMINAL_LEXEMES.keys():
        # match abstractions and applications, return appropriate productions
        if NON_TERMINAL_LEXEMES[key] == 'application':
            is_match, ndx = match_application(io)
    return io

# Core Interpreter Functions
def read(io):
    if io == '':
        io = input(">>> ")
    return io

def repl(io):
    while True:
        print(evaluate(read(io)))

if __name__ == '__main__':
    io = ''
    if len(sys.argv) > 1:
        io = sys.argv[1]
    print("---------- ge repl.py 0.1.0 ----------")
    signal(SIGINT, handler)
    repl(io)
