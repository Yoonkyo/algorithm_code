class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = sorted(nums)
        if a[0] + a[1] <= a[2]:
            return "none"

        result = ""
        if nums[0] == nums[1]:
            if nums[0] == nums[2]:
                result = "equilateral"
            else:
                result = "isosceles"
        elif nums[0] == nums[2]:
            result = "isosceles"
        elif nums[1] == nums[2]:
            result = "isosceles"
        else:
            result = "scalene"
        return result                
