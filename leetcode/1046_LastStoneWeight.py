class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones = stones[:-2] + [stones[-1]-stones[-2]]
        return stones[0]
