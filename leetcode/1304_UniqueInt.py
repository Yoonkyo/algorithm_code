class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = list(range(-(n//2), (n//2)+(n%2)))
        if n%2 == 0:
            result[-1] += n//2
        return(result)
