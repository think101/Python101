class Solution:
    def isValid(self, s: str) -> bool:
        d = []

        for c in s:
            if c in ['(', '[', '{']:
                d.insert(0, c)
            else:
                if not d:
                    return False

                x = d.pop(0)
                if not ((x == '(' and c == ')') or (x == '[' and c == ']') or (x == '{' and c == '}')):
                    return False

        return not d


t = Solution()
print(t.isValid("(){}[]"))

