from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        q = [0]
        res = 0
        cur = 0

        while q:
            res += 1

            l = len(q)
            m = q[l-1]
            for i in range(l):
                ind = q.pop(0)
                cur = max(cur, ind + nums[ind])
                if cur >= len(nums) - 1:
                    return res

                if m < cur:
                    for j in range(m + 1, cur + 1):
                        q.append(j)
                m = cur

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
    print(s.jump([3, 2, 1, 0, 4]))
    print(s.jump([0]))
    print(s.jump([2, 0, 0]))
