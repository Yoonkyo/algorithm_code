class Solution(object):
    def findFinalValue(self, nums, original):
        def findnum(nums, original):
            for i in nums:
                if original == i:
                    return original*2
            return original
        while True:
            new_number = findnum(nums, original)
            if original == new_number:
                return original
            else:
                original = new_number
