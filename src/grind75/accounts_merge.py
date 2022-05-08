from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # email to accounts indexes
        graph = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in graph:
                    graph.setdefault(accounts[i][j], [])

                graph[accounts[i][j]].append(i)

        visited = [False] * len(accounts)

        def dfs(i, s):
            if not visited[i]:
                name = accounts[i][0]

                visited[i] = True
                for j in range(1, len(accounts[i])):
                    s.add(accounts[i][j])
                    for neighbor in graph[accounts[i][j]]:
                        dfs(neighbor, s)

        res = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue

            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))

        return res

    def accountsMerge_dfs_TLE(self, accounts: List[List[str]]) -> List[List[str]]:
        # email to accounts indexes
        graph = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in graph:
                    graph.setdefault(accounts[i][j], [])

                graph[accounts[i][j]].append(i)

        visited = [False] * len(accounts)

        def dfs(email, li):
            if False not in visited:
                return []

            for i in graph[email]:
                if not visited[i]:
                    name = accounts[i][0]

                    visited[i] = True
                    if not li:
                        li = [name]
                    li = li + accounts[i][1:]
                    for j in range(1, len(accounts[i])):
                        li = li + dfs(accounts[i][j], li)[1:]

            return li

        res = []
        for email in graph:
            li = dfs(email, [])
            if li:
                res.append(li[0:1] + sorted(set(li[1:])))

        return res

    def accountsMerge_slow(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}

        for a in accounts:
            if a[0] not in d:
                d.setdefault(a[0], [])

            merged = a[1:]
            for i in range(1, len(a)):
                for j in range(len(d[a[0]])):
                    if d[a[0]][j] and a[i] in d[a[0]][j]:
                        merged = merged + d[a[0]][j]
                        d[a[0]][j] = None

            d[a[0]].append(merged)

        res = []
        for name in d:
            for emails in d[name]:
                if emails:
                    res.append([name] + sorted(set(emails)))

        return res

    def accountsMerge_wrong(self, accounts: List[List[str]]) -> List[List[str]]:
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
