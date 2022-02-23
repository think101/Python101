class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True
        elif n < 3 or n % 3 != 0:
            return False

        return self.isPowerOfThree(int(n / 3))


t = Solution()
test = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 0, 2, 5]
for i in test:
    print(t.isPowerOfThree(i))
