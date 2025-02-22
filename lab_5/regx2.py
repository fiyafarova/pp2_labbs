import re

with open("row.txt", "r") as file:
    text_to_match = file.read()


x = re.findall(r"ab{2,3}", text_to_match)

print(x)