class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n!=1:
            count = 0
            if n%2 == 0:
                n //= 2
                count += 1
            if n%3 == 0:
                n //= 3
                count += 1     
            if n%5 == 0:
                n //= 5
                count += 1           
            if count == 0:
                break
        
        if n == 1:
            return True
        else:
            return False
