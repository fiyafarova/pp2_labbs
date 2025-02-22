import re

with open("row.txt", "r") as file:
    text_to_match = file.read()


x = re.findall(r"a.+b", text_to_match)

print(x)