# pasta parser

right now it only does the parsing and builds a tree rather than interprets the tree and executes some stuff

## features:
- code comments with `//`
- functions with `identifier := { ... }`
- common math operators like `+`, `-`, `*`, `/`
- comparison operators like `==`, `>`, `<`
- logical operator `||`
- boolean values `true` and `false`
- strings with `"..."`
- integers

## research:

- [parser example cpp](https://www2.lawrence.edu/fast/GREGGJ/CMSC270/parser/parser.html)
- [right vs left recursion](https://www.ibm.com/docs/en/zvm/7.1?topic=topics-right-recursion-versus-left-recursion)
- [walrus operator](https://realpython.com/python-walrus-operator/)
- [antlr grammar example](https://stackoverflow.com/questions/1931307/antlr-is-there-a-simple-example)
- [left recursion wikipedia](https://en.wikipedia.org/wiki/Left_recursion)
- [importance of left recursion](https://medium.com/@eichenroth/the-importance-of-left-recursion-in-grammars-608f849447f6)
- [geeks for geeks how to remove left recursion](https://www.geeksforgeeks.org/removing-direct-and-indirect-left-recursion-in-a-grammar/)
- [cs course from jmu](https://w3.cs.jmu.edu/lam2mo/cs432_2017_08/files/04-grammars.pdf)
- [how to make grammar not ambiguous](https://stackoverflow.com/questions/38047734/make-a-context-free-grammar-not-ambiguous)