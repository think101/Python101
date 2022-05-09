class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')

        if not s:
            return 0

        sign = 0  # 0 no sign 1 positive 2 negative
        if s[0] in ["+", "-"]:
            sign = 2 if s[0] == "-" else 1

        end = 0
        start = 1 if sign else 0
        for i in range(start, len(s)):
            if not s[i:i+1].isdigit():
                end = i
                break
            else:
                end = i+1
        res = int(s[start:end]) if s[start:end] else 0
        res = res if sign in [0, 1] else -1 * res

        if res < - 2**31:
            res = -2**31
        if res > 2**31 - 1:
            res = 2**31 - 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
