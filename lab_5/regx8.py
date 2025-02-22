import re

text_to_match = "HelloWorldPythonRegex" 

pattern = r"[A-Z]" 

result = re.split(pattern, text_to_match) 

print(result)



