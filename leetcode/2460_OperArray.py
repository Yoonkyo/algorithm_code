class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        count = 0 
        while 0 in nums:
            nums.remove(0)
            count += 1
        result = nums + [0]*count
        return result
