from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq.setdefault(n, 0)
            freq[n] = freq.get(n) + 1

        freq_list = [None] * (len(nums)+1)
        for key, value in freq.items():
            if not freq_list[value]:
                freq_list[value] = []
            freq_list[value].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            if freq_list[i]:
                res.extend(freq_list[i])

            if len(res) >= k:
                break

        return res


t = Solution()
print(t.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(t.topKFrequent([1], 1))
