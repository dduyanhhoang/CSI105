import dis

compiled_code = compile("print('Hello, World!')", '<string>', 'exec')
dis.dis(compiled_code)

print(compiled_code)
