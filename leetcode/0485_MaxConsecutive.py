class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in nums:
            if i == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1
        result = max(result, count)
        return result
