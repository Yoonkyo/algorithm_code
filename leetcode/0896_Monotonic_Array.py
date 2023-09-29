class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a = 0
        b = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] > nums[i+1]:
                b = -1
            else:
                b = 1
            if a != b:
                if a == 0:
                    a = b
                else:
                    return False
        return True
