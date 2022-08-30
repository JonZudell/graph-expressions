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
TERMINAL_REGEX = OrderedDict()

GRAMMAR["<EXPRESSION>"] = ['graph-component',
                           '( <EXPRESSION> )',
                           '( <EXPRESSION> <EXPRESSION> )',
                           '( λ graph-component . <EXPRESSION>)']

TERMINAL_REGEX["graph-component"] = r'[a-z](-[a-z])?'

LAMBDA_SYMBOL='λ'
CURRENT_SYMBOL="<EXPRESSION>"

# Helpers
def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def format_expression(func):
    def wrapper(expression):
        func(re.sub(r'\s+', ' ', expression).lower().strip(' '))
    return wrapper

def evaluate(io):
    # match parens recursively until you bottom out
    # once an expression has bottomed out rewrite on the way up
    return io

def repl(io):
    while True:
        print(evaluate(read(io)))

# Core Interpreter Functions
def read(io):
    if io == '':
        io = input(">>> ")
    return io

if __name__ == '__main__':
    io = ''
    if len(sys.argv) > 1:
        io = sys.argv[1]
    print("---------- ge repl.py 0.0.0 ----------")
    signal(SIGINT, handler)
    repl(io)
