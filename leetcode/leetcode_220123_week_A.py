class Solution:
    def countElements(self, nums: List[int]) -> int:
        result = 0
        mini = min(nums)
        maxi = max(nums)
        for i in nums:
            if i > mini and i < maxi:
                result += 1
        return result
