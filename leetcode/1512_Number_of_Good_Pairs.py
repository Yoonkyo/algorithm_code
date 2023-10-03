class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        for i in range(0, length):
            for j in range(i+1, length):
                if nums[i] == nums[j]:
                    result += 1
        return result
