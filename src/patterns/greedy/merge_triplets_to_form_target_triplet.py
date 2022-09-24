from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0] * 3

        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                if triplets[i][0] == target[0]:
                    res[0] = 1
                if triplets[i][1] == target[1]:
                    res[1] = 1
                if triplets[i][2] == target[2]:
                    res[2] = 1

                if res[0] == 1 and res[1] == 1 and res[2] == 1:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
    print(s.mergeTriplets([[1, 3, 4], [2, 5, 8]], [2, 5, 8]))
    print(s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))
    print(s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
