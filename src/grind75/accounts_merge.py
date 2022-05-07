from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}

        for a in accounts:
            if a[0] not in d:
                d.setdefault(a[0], [])

            merged = False
            for i in range(1, len(a)):
                for j in range(len(d[a[0]])):
                    if a[i] in d[a[0]][j]:
                        d[a[0]][j] = d[a[0]][j] + a[1:]
                        merged = True
                        break

                if merged:
                    break

            if not merged:
                d[a[0]].append(a[1:])

        res = []
        for name in d:
            for emails in d[name]:
                res.append([name] + sorted(set(emails)))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.accountsMerge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
