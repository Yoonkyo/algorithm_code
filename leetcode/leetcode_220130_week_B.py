class Solution(object):
    def maxScoreIndices(self, nums):
        nums_left = 0
        nums_right = nums.count(1)  
        max_value = nums_right
        result = [0]
        for i in range(len(nums)):
            check = nums[i]
            if check == 0:
                nums_left += 1
            elif check == 1:
                nums_right -= 1
            score = nums_left + nums_right
            if score > max_value:
                result = [i+1]
                max_value = score
            elif score == max_value:
                result.append(i+1)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
