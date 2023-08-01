from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n_list = list(range(1,n+1))
        answer = combinations(n_list, k)
        return answer
