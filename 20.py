def isValid(self, s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']':
            if not stack:
                return False
            o = stack.pop()
            if c == ')' and o != '(':
                return False
            elif c == '}' and o != '{':
                return False
            elif c == ']' and o != '[':
                return False

    return len(stack) == 0