class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '{':
                stack.append(c)
            elif c == '[':
                stack.append(c)
            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if ((top == '(' and c != ')') or
                       (top == '{' and c != '}') or
                       (top == '[' and c != ']')):
                       return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
