# C

Source program: [hello.c](./hello.c)

Compiler: GCC

## Lexical analysis

The GCC's main function is to analyze the source code and divide it into tokens, with instructions closely intertwined within the compiler and primarily linked to the compilation procedure. A helpful way to find keywords is by referring to detailed language documentation like the [GNU C reference manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html) and [C reference](https://en.cppreference.com/w/c). These resources do not cover lexical analysis in a theoretical manner but provide guidance on utilizing the compiler to influence the compilation process and leveraging the programming language.

## Syntax analysis

The GCC compiler offers the `-fdump-tree-original-raw` flag to generate a thorough linear representation of the Abstract Syntax Tree (AST) used in the compilation process. The result file is named [a-hello.c.005t.original](./a-hello.c.005t.original). The [graph view](./AST.png) of this AST is, therefore, super detailed. A more straightforward demonstration could be the following diagram [this](./AST_simple.tex).

## Semantic analysis

The AST generated in the syntax analysis phase is used for semantic checking. To assure semantic consistency, the Linux `man` command and other detailed documentation explain the functions and types in detail, even if much of the work is not visible. They offer not just the standard language information but also documentation for other libraries. For instance, it is handy to use the command `print(1)` in Python to display the number 1 on the screen. When using `printf()` in C, calling `printf(1)` will result in a warning during compilation and a segmentation fault during execution. This occurs because the `printf` function is documented to expect an argument of type `const char *format`, which is a string with optional formatting.

```c
#include <stdio.h>


int main() {
	printf(1);

	return 0;
}


```

```c
➜  err_test gcc main.c -o main
main.c: In function ‘main’:
main.c:5:16: warning: passing argument 1 of ‘printf’ makes pointer from integer without a cast [-Wint-conversion]
    5 |         printf(1);
      |                ^
      |                |
      |                int
In file included from main.c:1:
/usr/include/stdio.h:356:43: note: expected ‘const char * restrict’ but argument is of type ‘int’
  356 | extern int printf (const char *__restrict __format, ...);
      |                    ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~
main.c:5:9: warning: format not a string literal and no format arguments [-Wformat-security]
    5 |         printf(1);
      |         ^~~~~~
➜  err_test ./main                                                     
[1]    29653 segmentation fault (core dumped)  ./main
```

## Code generation

The syntactically correct source code is compiled into the executable file, making it comprehensible and executable by a computer. To view the machine code, you can use the `xxd` command to generate a hexadecimal dump of the executable file located at [hello_hexdump.hex](./hello_hexdump.hex). The hexadecimal instructions consist of around one thousand lines to execute five lines of C code. For a clearer understanding, examine the [assembly representation](./hello_asm.asm) of the file, which consists of over a hundred lines of code. Despite the difficulties, the code's output is anticipated from the start and is straightforward. Displaying the text "Hello, World!" on the screen signifies the completion of converting a high-level language into machine code execution.

```sh
➜  C ./hello 
Hello, World!
```