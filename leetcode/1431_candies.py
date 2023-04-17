class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [0] * len(candies)
        max_value = max(candies)
        for i, num in enumerate(candies):
            if num+extraCandies < max_value:
                result[i] = False
            else:
                result[i] = True
        return result
