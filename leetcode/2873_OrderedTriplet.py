class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_result = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i]-nums[j])*nums[k] > max_result:
                        max_result = (nums[i]-nums[j])*nums[k]
        return max_result
