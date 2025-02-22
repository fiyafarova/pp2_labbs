import re

def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

text_to_match = "HelloWorldPythonRegex"

new = insert_spaces(text_to_match) #added spaces between words


result = re.split(r' ', new) #split by space


print(result) 
