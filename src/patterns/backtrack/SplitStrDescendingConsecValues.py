class Solution:
    def splitString(self, s: str) -> bool:
        parts = []

        def dfs(i):
            if i == len(s) and len(parts) > 1:
                return True

            for j in range(i, len(s)):
                if len(parts) == 0 or parts[-1] - int(s[i:j+1]) == 1:
                    parts.append(int(s[i:j+1]))
                    if dfs(j+1):
                        return True
                    parts.pop()

            return False

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    print(s.splitString("050043"))
    print(s.splitString("00"))



