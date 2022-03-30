class Solution:
    def isValid(self, s: str) -> bool:
        q = []

        for c in s:
            if c in ['(', '[', '{']:
                q.insert(0, c)
            else:
                t = q.pop(0) if q else None
                if (c == ')' and t != '(') or (c == ']' and t != '[') or (c == '}' and t != '{'):
                    return False

        return not q

