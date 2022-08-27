# repl.py
# -----------------------------------------------------------------------------
# graph-expression
#   A context-free, unambiguous, recursive grammar
#   no left recursion, left factored.
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
# Parser
#   Non Deterministic Pushdown Automota
# -----------------------------------------------------------------------------
# Needs:
# - io
# - import
# - package structure

import sys
import re
START_SYMBOL="<ATOM>"
GRAMMAR = {}
GRAMMAR["<ATOM>"] = ['<EXPRESSION>', 'variable']
GRAMMAR["<EXPRESSION>"] = ['"("<ATOM>")"', '<ABSTRACTION>','<APPLICATION>']
GRAMMAR["<ABSTRATION>"] = ['lambda <ATOM> dot <ATOM>']
GRAMMAR["<APPLICATION>"] = ['<ATOM>', '<APPLICATION> (<ATOM> | <ABSTRACTION>)']

def read():
    return input("")

def evaluate(expression):
    pass

while True:
    print(evaluate(read()))
