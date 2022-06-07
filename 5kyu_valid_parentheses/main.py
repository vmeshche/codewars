def valid_parentheses(string):

    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        if s == ")":
            try:
                stack.pop()
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(valid_parentheses("())(()"))