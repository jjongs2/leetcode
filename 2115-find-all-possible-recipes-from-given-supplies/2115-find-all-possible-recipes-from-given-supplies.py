from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        ingredients = list(map(set, ingredients))
        d = defaultdict(list)
        for i, ingredient in enumerate(ingredients):
            for x in ingredient:
                d[x].append(i)
        result = []
        q = deque(supplies)
        while q:
            x = q.popleft()
            for i in d[x]:
                ingredients[i].remove(x)
                if not ingredients[i]:
                    q.append(recipes[i])
                    result.append(recipes[i])
        return result
