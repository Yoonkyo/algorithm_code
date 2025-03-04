class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 3:
            remainder = n%3
            n //= 3
            if remainder == 2:
                return False
        if n == 2:
            return False
        else:
            return True
