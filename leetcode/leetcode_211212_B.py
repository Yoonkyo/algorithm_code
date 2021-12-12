class Solution(object):
    def subArrayRanges(self, nums):
        length = len(nums)
        result = 0
        for i in range(length):
            for j in range(i, length):
                temp_list = nums[i:j+1]
                result += max(temp_list)-min(temp_list)
        return result
        
        """
        :type nums: List[int]
        :rtype: int
        """
