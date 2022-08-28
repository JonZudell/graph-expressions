# graph-expressions
A toy programming language with syntax inspired by the lambda calculus.

With the goal of implementing a context-free, unambiguous, recursive grammar.

As a no left recursion, left factored language. Read it like polish notation arithmatic.

Everything is an identity or terminal symbol, a symbol never before encountered will be added to the graph and return itself.

## Abstract rewriting system
> It's been theorized since 6 BCE by Sanskrit scholars that any language structure can be described by the continuous application of symbol substition rules.
Language is a system for computation. Grammar defines the structure of language. 
Using a grammar and symbolic representations of [Combinational Login](https://en.wikipedia.org/wiki/Combinational_logic) we can compute anything.
Either by defering execution to the `REPL` or using pure logic operations on an input.

## Definiton of Grammar
[CS-340](https://ycpcs.github.io/cs340-fall2016/labs/index.html)
[Grammar Theory](https://www.geeksforgeeks.org/introduction-to-grammar-in-theory-of-computation/)
> Formal Definition of Grammar :
> Any Grammar can be represented by 4 tuples – <N, T, P, S>
>
>  N – Finite Non-Empty Set of Non-Terminal Symbols.
>  T – Finite Set of Terminal Symbols.
>  P – Finite Non-Empty Set of Production Rules.
>  S – Start Symbol (Symbol from where we start producing our sentences or strings).
If it has more than four tuples involved maybe rethink it.

## Backus-Naur Form
Backus-Naur Form is an abstract grammar definition. Unpack Symbols until you hit a terminal symbol, apply the production rule..
```<symbol> ::= __expression__```

### graph-expression grammar-rules
```
Grammar for the lambda-calculus
  <ATOM>        ::= <EXPRESSION> | variable
  <EXPRESSION>  ::= "("<ATOM>")" | <ABSTRACTION> | <APPLICATION>>
  <ABSTRATION>  ::= lambda <ATOM> dot <ATOM>
  <APPLICATION> ::= <ATOM> | <APPLICATION> (<ATOM>| <ABSTRACTION>)
```

## Encoding Data
[CS-311](https://www.cs.rice.edu/~javaplt/311/Readings/supplemental.pdf)
[Church Encoding](https://en.wikipedia.org/wiki/Church_encoding)
> Terms that are usually considered primitive in other notations (such as integers, booleans, pairs, lists, and tagged unions) are mapped to higher-order functions under Church encoding. 
Bootstrapping types from combinational logic.
