import re

with open("row.txt", "r") as file:
    text_to_match = file.read()


x = re.findall(r"\b[a-z]+_[a-z]+\b", text_to_match)

print(x)