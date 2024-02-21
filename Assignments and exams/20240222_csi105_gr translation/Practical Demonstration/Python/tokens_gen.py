import tokenize
from io import BytesIO

code = 'print("Hello, World!")'
tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))

for token in tokens:
    print(token)
