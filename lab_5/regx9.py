import re

def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

text_to_match = "HelloWorldPythonRegex"
result = insert_spaces(text_to_match)

print(result) 
