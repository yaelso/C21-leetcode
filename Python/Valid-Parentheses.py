def isValid(s):
    if not len(s) % 2 == 0:
        return False

    guide = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack = []

    for bracket in s:
        if bracket in guide.keys():
            stack.append(bracket)
        elif len(stack) == 0 or not bracket == guide[stack.pop()]:
            return False
    return stack == []

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(}")) # False
