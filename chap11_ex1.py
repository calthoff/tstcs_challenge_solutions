def check_parenthesis(a_string):
    paren_stack = []
    bracket_stack = []
    for c in a_string:
        if c == '(':
            paren_stack.append(c)
        if c == '{':
            bracket_stack.append(c)
        if c == ')':
            if len(paren_stack) == 0:
                return False
            else:
                paren_stack.pop()
        if c == '}':
            if len(bracket_stack) == 0:
                return False
            else:
                bracket_stack.pop()
    return len(paren_stack) == 0 and len(bracket_stack) == 0

print(check_parenthesis('(()){}{{}}()'))