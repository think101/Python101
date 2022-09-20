from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        res = 0

        while nums_s:
            r = 0

            i = nums_s.pop()
            r += 1

            inc = i
            while nums_s and inc + 1 in nums_s:
                inc += 1
                r += 1
                nums_s.remove(inc)

            dec = i
            while nums_s and dec - 1 in nums_s:
                dec -= 1
                r += 1
                nums_s.remove(dec)

            res = max(r, res)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
