from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(visited, i):
            if i == len(s):
                res.append(''.join(visited))
                return

            if not s[i].isalpha():
                visited.append(s[i])
                backtrack(visited, i+1)
                visited.pop()
            else:
                visited.append(s[i].lower())
                backtrack(visited, i+1)
                visited.pop()

                visited.append(s[i].upper())
                backtrack(visited, i+1)
                visited.pop()

        backtrack([], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("3z4"))


# it is important to have the line 16 to do the pop() operation
