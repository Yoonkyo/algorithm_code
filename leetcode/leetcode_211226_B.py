class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        result = []
        new_result = []
        recipes_num = len(recipes)
        for i in range(recipes_num):
            supplies_set = set(supplies)
            if set(ingredients[i]) <= supplies_set:
                result.append(recipes[i])
                supplies.append(recipes[i])
                
        while new_result == []:
            for i in range(recipes_num):
                if recipes[i] in result:
                    continue
                else:
                    supplies_set = set(supplies)
                    if set(ingredients[i]) <= supplies_set:
                        new_result.append(recipes[i])
                        supplies.append(recipes[i])
            if new_result != []:
                for extra in new_result:
                    result.append(extra)
                new_result = []
            else:
                break
        return result
            
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        
