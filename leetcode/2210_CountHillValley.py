class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        same = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                same += 1
                continue
            if nums[i] > nums[i-1-same] and nums[i] > nums[i+1]:
                result += 1
            elif nums[i] < nums[i-1-same] and nums[i] < nums[i+1]:
                result += 1
            same = 0
        return result
