from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = {}  # 0:visited 1:visiting 2:cycle
        neighbors = {}

        for list_elem in prerequisites:
            if list_elem[1] not in neighbors:
                neighbors[list_elem[1]] = []
            neighbors[list_elem[1]].append(list_elem[0])

        def dfs(course: int) -> int:
            if course in status:
                if status[course] == 0:
                    return 0
                elif status[course] == 1:
                    return 2

            status[course] = 1
            if course in neighbors:
                for neighbor in neighbors[course]:
                    r = dfs(neighbor)
                    if r == 2:
                        return 2

            status[course] = 0
            return 0

        for i in range(numCourses):
            res = dfs(i)
            if res == 2:
                return False

        return True

t = Solution()
print(t.canFinish(2, [[1,0]]))
print(t.canFinish(2, [[1,0],[0,1]]))
print(t.canFinish(2, [[1,0],[0,1],[0,0]]))
print(t.canFinish(6, [[1,0],[2,1],[3,2]]))

