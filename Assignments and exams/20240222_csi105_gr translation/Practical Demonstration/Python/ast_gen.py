import ast

code_ast = ast.parse("print('Hello, World!')")
print(ast.dump(code_ast, indent=4))
