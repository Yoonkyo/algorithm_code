class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s_nums = sorted(nums)
        for i in range(n):
            if s_nums[i] != i:
                return i
        return n
