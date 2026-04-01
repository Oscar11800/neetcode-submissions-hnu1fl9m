class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = "[{("
        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ']':
                    if top != '[':
                        return False
                elif c == ')':
                    if top != '(':
                        return False
                else:
                    if top != '{':
                        return False
        return not stack