class Solution(object):
    def subArrayRanges(self, nums):
        length = len(nums)
        result = 0
        for i in range(length):
            max_num = nums[i]
            min_num = nums[i]
            for j in range(i+1, length):
                max_num = max(max_num, nums[j])
                min_num = min(min_num, nums[j])
                result += max_num - min_num
        return result
        
        """
        :type nums: List[int]
        :rtype: int
        """
