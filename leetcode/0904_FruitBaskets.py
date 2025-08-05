class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 1
        for n in range((len(fruits))-1):
            count = 0
            basket = []
            for i in range(n, len(fruits)):
                if len(basket) < 2 and fruits[i] not in basket:
                    basket.append(fruits[i])
                    count += 1
                    continue
                elif fruits[i] in basket:
                    count += 1
                else:
                    break
            if result < count:
                result = count
                count = 0
            if result >= len(fruits)-n:
                return result
        return result 
