from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i - 1 >= 0 and arr[i] == arr[i - 1]:
                continue
            if arr[i] == arr[i + len(arr) // 4]:
                return arr[i]

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 7]))
