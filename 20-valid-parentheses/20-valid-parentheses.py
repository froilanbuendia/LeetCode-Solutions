class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        if len(s) == 1:
            return False
        for i in s:
            if i in ['(', '[', '{']:
                l.append(i)
            elif len(l) == 0:
                return False
            elif i == ')' and '(' in l[-1]:
                l.pop()
            elif i == ']' and '[' in l[-1]:
                l.pop()
            elif i == '}' and '{' in l[-1]:
                l.pop()
            else:
                return False
        if len(l) > 0:
            return False
        return True