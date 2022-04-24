from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_r = Counter(ransomNote)
        c_m = Counter(magazine)

        for i in ransomNote:
            if c_r[i] > c_m[i]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "ab"))
    print(s.canConstruct("aa", "aab"))