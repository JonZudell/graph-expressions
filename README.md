# graph-expressions
A toy programming language with syntax inspired by the lambda calculus.

Everything is an identity or terminal symbol, a symbol never before encountered will be added to the graph.

## Abstract rewriting system
[Formal Grammer](https://en.wikipedia.org/wiki/Formal_grammar)
[Abstract Rewrite System](https://en.wikipedia.org/wiki/Abstract_rewriting_system)
Grammars are used to describe the structure of a languae and the Abstract Rewriting System describes how to apply them. Like Algebra.

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
<expression> ::= <variable>                      ; lowercase identifiers
               | <constant>                      ; predefined objects
               | ( <expression> <expression> )   ; combinations
               | ( λ <variable> . <expression> ) ; abstractions
```

## Encoding Data
[CS-311](https://www.cs.rice.edu/~javaplt/311/Readings/supplemental.pdf)
[Church Encoding](https://en.wikipedia.org/wiki/Church_encoding)
> Terms that are usually considered primitive in other notations (such as integers, booleans, pairs, lists, and tagged unions) are mapped to higher-order functions under Church encoding. 
Bootstrapping types from combinational logic.
