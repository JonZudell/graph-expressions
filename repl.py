# repl.py
# -----------------------------------------------------------------------------
# Interpreter
#   Non Deterministic Pushdown Automota
#   Read Evaluate Print Loop
import sys
import re
from signal import signal, SIGINT


GRAMMAR = {}
TERMINAL_REGEX = {}

GRAMMAR["<ATOM>"] = ['graph-component', '<EXPRESSION>', '<ABSTRACTION>','<APPLICATION>']
GRAMMAR["<ABSTRATION>"] = ['lambda <ATOM> dot <ATOM>']
GRAMMAR["<APPLICATION>"] = ['<ATOM>', '<APPLICATION> (<ATOM>|<ABSTRACTION>)']

TERMINAL_REGEX["graph-component"] = r'([a-z]*)(-[a-z]+)'
TERMINAL_REGEX["lambda"] = r'(lambda|λ)'
TERMINAL_REGEX["dot"] = r'(dot|.)'

LAMBDA_SYMBOL='λ'
CURRENT_SYMBOL="<ATOM>"
GRAPH = {}

def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def read(io):
    if io == '':
        io = input(">>> ")
    return io

#def format_expression(func):
#    def wrapper(expression):
#        func(re.sub(r'\s+', ' ', expression).lower().strip(' '))
#    return wrapper

#@format_expression
def evaluate(io):
    for key in GRAMMAR.keys():
        if re.match(key, io):
            print("non-terminal")
            return key
    for key in TERMINAL_REGEX.keys():
        if re.match(TERMINAL_REGEX[key], io):
            print("terminal")
            return io
    else:
        print("# non-terminal")
        return io 
        # pass update symbol and pop the 'Symbol off the stack;
    #    print(expression)
    #elif re.match('{' + '|'.join(TERMINAL_REGEX.keys()) + '}'):
        # atom apply value to next
    #    print(expression)
    #    pass
    #elif expression.starts_with('l'):
        # anonymous function declaration
    #    pass
    #else:
        # add new symbol to graph
    #    pass


def repl(io):
    while True:
        print(evaluate(read(io)))

if __name__ == '__main__':
    io = ''
    if len(sys.argv) > 1:
        io = sys.argv[1]
    print("---------- ge repl.py 0.0.0 ----------")
    signal(SIGINT, handler)
    repl(io)
