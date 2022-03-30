class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s if i.isalpha() or i.isnumeric()]).lower()

        return s == s[::-1]


# Test
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("0P"))
