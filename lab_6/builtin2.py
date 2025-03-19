def count(s):
    up= sum(1 for char in s if char.isupper())
    low = sum(1 for char in s if char.islower())
    print(f"Uppercase: {up}")
    print(f"Lowercase: {low}")

text = input()
count(text)
