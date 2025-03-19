def isAllTrue(elements):
    return all(elements)

print(isAllTrue((True, 1, True, "string")))
print(isAllTrue((True, 0, True)))