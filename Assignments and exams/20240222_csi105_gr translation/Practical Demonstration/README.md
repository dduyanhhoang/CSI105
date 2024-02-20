# C

Source program: [hello.c](./hello.c)

Compiler: GCC

## Lexical analysis

While the purpose of GCC is scanning the source program and breaking it down into tokens, the instructions is deeply integrated inside the compiler and mostly related to compilation process. The more approachable of looking for keywords is using the comprehensive language documetations such as [GNU C reference manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html) and [C reference](https://en.cppreference.com/w/c). While these resources do not discuss lexical analysis in the theoratical sense, they offer insights into how to use the compiler affect the compilation process, and to use the use the programming language itself.

## Syntax analysis

GCC provide `-fdump-tree-original-tree` flag to output the file [a-hello.c.005t.original](./a-hello.c.005t.original) which is a quite detailed linear representation of AST used by GCC during the compilation process. The [graph view](./AST.png) of this AST is therefore super detailed. A simpler demonstration could be done by [this](./AST_simple.tex).
