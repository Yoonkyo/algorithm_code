class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        while nums:
            i = nums[0]
            try:
                nums.remove(i)
                nums.remove(i)
            except ValueError:
                return False
        return True