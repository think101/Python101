from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in d:
                d.setdefault(sorted_s, [])
            d[sorted_s].append(s)

        return list(d.values())


t = Solution()
print(t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))