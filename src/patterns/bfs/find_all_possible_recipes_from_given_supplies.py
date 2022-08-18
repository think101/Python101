from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        reSet, suSet = set(recipes), set(supplies)
        prereq = {}
        reverse_prereq = {}
        res = set()
        q = []

        for i in range(len(recipes)):
            r = recipes[i]
            can_create = True
            for ingre in ingredients[i]:
                if ingre not in suSet and ingre not in reSet:
                    can_create = False
                    break

                if ingre in reSet:
                    if r not in prereq:
                        prereq[r] = set()
                    if ingre not in reverse_prereq:
                        reverse_prereq[ingre] = set()

                    prereq[r].add(ingre)
                    reverse_prereq[ingre].add(r)

                if can_create:
                    q.append(r)

        while q:
            r = q.pop()
            res.add(r)

            if r in reverse_prereq:
                for t in reverse_prereq[r]:
                    prereq[t].remove(r)
                    if not prereq[t]:
                        q.append(t)

        return list(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]))

