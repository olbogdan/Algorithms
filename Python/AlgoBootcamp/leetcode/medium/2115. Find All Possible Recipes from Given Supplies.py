# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
#
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
#
# Return a list of all the recipes that you can create. You may return the answer in any order.
#
# Note that two recipes may contain each other in their ingredients.
#
#
#
# Example 1:
#
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# Example 2:
#
# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# Example 3:
#
# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
#
#
# Constraints:
#
# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.
from collections import defaultdict
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indr = {}
        for i in range(len(recipes)):
            indr[recipes[i]] = len(ingredients[i])
        adj = defaultdict(list)
        for i in range(len(ingredients)):
            for ingr in ingredients[i]:
                adj[ingr].append(recipes[i])
        res = []
        while supplies:
            sup = supplies.pop()
            for parent in adj[sup]:
                indr[parent] -= 1
                if indr[parent] == 0:
                    supplies.append(parent)
                    res.append(parent)
        return res


sol = Solution()
assert sol.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]) == ["bread"]


class Solution2:
    def findAllRecipes(self, recipesList: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recipes = {}
        for i in range(len(recipesList)):
            recipes[recipesList[i]] = ingredients[i]
        res = []
        def findAvailable():
            foundItem = None
            for key, val in recipes.items():
                foundI = 0
                for need in val:
                    if need not in supplies:
                        break
                    foundI += 1
                if foundI == len(val):
                    foundItem = key
                    break
            if foundItem is None:
                return False
            else:
                supplies.add(foundItem)
                del recipes[foundItem]
                res.append(foundItem)
                return True
        while findAvailable() is True:
            print("built recipe")
        return res


s = Solution2()
assert s.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]) == ["bread"]
