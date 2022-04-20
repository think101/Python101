class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))