class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        for fruit in fruits:
            check = 0
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    check = 1
                    break
            if check == 0:
                result += 1
        return result
