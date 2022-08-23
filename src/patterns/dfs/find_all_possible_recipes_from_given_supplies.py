from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set, sup_set = set(recipes), set(supplies)
        prereqs = {}
        decided = {}
        res = set()

        for i in range(len(ingredients)):
            prereqs[recipes[i]] = ingredients[i]

        def dfs(recipe, visited):
            if recipe in decided:
                return decided[recipe]

            if recipe in visited:
                decided[recipe] = False
                return False

            for ing in prereqs[recipe]:
                if not (ing in sup_set or ing in recipes_set):
                    decided[recipe] = False
                    return False

                if ing in recipes_set:
                    visited.append(recipe)
                    r = dfs(ing, visited)
                    visited.pop()

                    if not r:
                        decided[recipe] = False
                        return False

            decided[recipe] = True
            res.add(recipe)
            return True

        for recipe in recipes:
            dfs(recipe, [])

        return list(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]))
    print(sol.findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"]))
    print(sol.findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "meat", "corn"]))
