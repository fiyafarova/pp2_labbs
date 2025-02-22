import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

camel_string = "helloWorldPythonRegex"
snake_case_string = camel_to_snake(camel_string)

print(snake_case_string)
