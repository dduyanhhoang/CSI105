# Python

CPython, a widely used interpreter for Python, is written in C and is activated by typing `python` or `python3` in the terminal. The python translation process is managed internally, similar to C. Python language provides various number of libraries that reveal those hidden processes, which can be accessed by default or installed via `pip`, a Python package installer. Package documentation can be accessed on the `pypi` website or locally with `pydoc`.

## Lexical analysis

```python
import tokenize
from io import BytesIO

code = 'print("Hello, World!")'
tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))

for token in tokens:
    print(token)
```

```
TokenInfo(type=63 (ENCODING), string='utf-8', start=(0, 0), end=(0, 0), line='')
TokenInfo(type=1 (NAME), string='print', start=(1, 0), end=(1, 5), line='print("Hello, World!")')
TokenInfo(type=54 (OP), string='(', start=(1, 5), end=(1, 6), line='print("Hello, World!")')
TokenInfo(type=3 (STRING), string='"Hello, World!"', start=(1, 6), end=(1, 21), line='print("Hello, World!")')
TokenInfo(type=54 (OP), string=')', start=(1, 21), end=(1, 22), line='print("Hello, World!")')
TokenInfo(type=4 (NEWLINE), string='', start=(1, 22), end=(1, 23), line='')
TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='')
```

## Syntax analysis and semantic analysis

```python
import ast

code_ast = ast.parse("print('Hello, World!')")
print(ast.dump(code_ast, indent=4))
```

```
Module(
    body=[
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Constant(value='Hello, World!')],
                keywords=[]))],
    type_ignores=[])
```

## Code generation

Python is an interpreted language; therefore, in this last step, translated bytecode is handled by the Python virtual machine, which takes most of the heavy lifting work.

```python
import dis

compiled_code = compile("print('Hello, World!')", '<string>', 'exec')
dis.dis(compiled_code)

print(compiled_code)
```

```
  0           0 RESUME                   0

  1           2 PUSH_NULL
              4 LOAD_NAME                0 (print)
              6 LOAD_CONST               0 ('Hello, World!')
              8 PRECALL                  1
             12 CALL                     1
             22 POP_TOP
             24 LOAD_CONST               1 (None)
             26 RETURN_VALUE
<code object <module> at 0x000001C6ED80E790, file "<string>", line 1>
```
