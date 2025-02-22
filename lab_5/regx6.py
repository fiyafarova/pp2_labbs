import re

text_to_replace = "Hello, world. This is a test."

newtext = re.sub(r"[ ,\.]", ':',text_to_replace)

print(newtext)
